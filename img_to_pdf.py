#!/usr/bin/env python3
"""
画像ファイルをPDFに変換するスクリプト
"""
import argparse
import os
import sys
from pathlib import Path
from PIL import Image


def get_image_files(directory):
    """
    指定されたディレクトリから対応する画像ファイルを取得し、昇順でソートする
    
    Args:
        directory (str): 画像ファイルが格納されているディレクトリパス
        
    Returns:
        list: ソートされた画像ファイルのパスリスト
    """
    supported_extensions = {'.bmp', '.jpg', '.jpeg', '.png', '.tiff', '.tif'}
    image_files = []
    
    dir_path = Path(directory)
    if not dir_path.exists():
        raise FileNotFoundError(f"ディレクトリが見つかりません: {directory}")
    
    if not dir_path.is_dir():
        raise NotADirectoryError(f"指定されたパスはディレクトリではありません: {directory}")
    
    for file_path in dir_path.iterdir():
        if file_path.is_file() and file_path.suffix.lower() in supported_extensions:
            image_files.append(file_path)
    
    # ファイル名で昇順にソート
    image_files.sort(key=lambda x: x.name)
    
    return image_files


def convert_images_to_pdf(image_files, output_path):
    """
    画像ファイルリストを1つのPDFファイルに変換する
    
    Args:
        image_files (list): 画像ファイルのパスリスト
        output_path (str): 出力PDFファイルのパス
    """
    if not image_files:
        raise ValueError("変換する画像ファイルが見つかりません")
    
    # 最初の画像を開く
    first_image = Image.open(image_files[0])
    
    # RGBモードに変換（PDFに保存する場合はRGBが必要）
    if first_image.mode != 'RGB':
        first_image = first_image.convert('RGB')
    
    # 残りの画像を処理
    rgb_images = []
    for image_path in image_files[1:]:
        img = Image.open(image_path)
        if img.mode != 'RGB':
            img = img.convert('RGB')
        rgb_images.append(img)
    
    # PDFとして保存
    if rgb_images:
        first_image.save(
            output_path,
            'PDF',
            save_all=True,
            append_images=rgb_images
        )
    else:
        first_image.save(output_path, 'PDF')
    
    # メモリ解放
    first_image.close()
    for img in rgb_images:
        img.close()


def main():
    """メイン関数"""
    parser = argparse.ArgumentParser(
        description='画像ファイルを1つのPDFファイルに変換します',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
使用例:
  python img_to_pdf.py /path/to/images
  python img_to_pdf.py /path/to/images -o output.pdf
  python img_to_pdf.py /path/to/images --output my_document.pdf
        '''
    )
    
    parser.add_argument(
        'input_dir',
        help='画像ファイルが格納されているディレクトリパス'
    )
    
    parser.add_argument(
        '-o', '--output',
        default='output.pdf',
        help='出力PDFファイル名（デフォルト: output.pdf）'
    )
    
    args = parser.parse_args()
    
    try:
        # 画像ファイルを取得
        print(f"ディレクトリを検索中: {args.input_dir}")
        image_files = get_image_files(args.input_dir)
        
        if not image_files:
            print("エラー: 対応する画像ファイルが見つかりませんでした")
            print("対応フォーマット: .bmp, .jpg, .jpeg, .png, .tiff, .tif")
            sys.exit(1)
        
        print(f"見つかった画像ファイル数: {len(image_files)}")
        for img_file in image_files:
            print(f"  - {img_file.name}")
        
        # PDFに変換
        print(f"\nPDFに変換中...")
        convert_images_to_pdf(image_files, args.output)
        
        # 出力ファイルの絶対パスを取得
        output_abs_path = Path(args.output).resolve()
        print(f"\n完了: {output_abs_path}")
        
    except Exception as e:
        print(f"エラー: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
