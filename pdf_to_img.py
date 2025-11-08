#!/usr/bin/env python3
"""
PDFファイルを画像ファイルに変換するスクリプト
"""
import argparse
import os
import sys
from pathlib import Path
import fitz  # PyMuPDF


def convert_pdf_to_images(pdf_path, output_dir, dpi=300):
    """
    PDFファイルの各ページをPNG画像として保存する
    
    Args:
        pdf_path (str): 入力PDFファイルのパス
        output_dir (str): 出力先ディレクトリのパス
        dpi (int): 画像の解像度（デフォルト: 300）
        
    Returns:
        list: 生成された画像ファイルのパスリスト
    """
    # PDFファイルを開く
    pdf_document = fitz.open(pdf_path)
    page_count = len(pdf_document)
    
    # 出力先ディレクトリを作成
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    
    # ページ数に応じて桁数を決定（最低3桁）
    digit_count = max(3, len(str(page_count)))
    
    output_files = []
    
    # 各ページを画像として保存
    for page_num in range(page_count):
        # ページを取得
        page = pdf_document[page_num]
        
        # DPIに基づいてズーム倍率を計算（デフォルトは72 DPI）
        zoom = dpi / 72
        mat = fitz.Matrix(zoom, zoom)
        
        # ページを画像に変換
        pix = page.get_pixmap(matrix=mat)
        
        # ファイル名を生成（000.png, 001.png, ...）
        output_filename = f"{page_num:0{digit_count}d}.png"
        output_filepath = output_path / output_filename
        
        # PNG形式で保存
        pix.save(str(output_filepath))
        output_files.append(output_filepath)
        
        print(f"ページ {page_num + 1}/{page_count} を保存: {output_filename}")
    
    # メモリ解放
    pdf_document.close()
    
    return output_files


def main():
    """メイン関数"""
    parser = argparse.ArgumentParser(
        description='PDFファイルの各ページをPNG画像として出力します',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
使用例:
  python pdf_to_img.py document.pdf
  python pdf_to_img.py document.pdf -o output_images
  python pdf_to_img.py document.pdf --output ./images --dpi 150
        '''
    )
    
    parser.add_argument(
        'input_pdf',
        help='変換対象のPDFファイルパス'
    )
    
    parser.add_argument(
        '-o', '--output',
        default='.',
        help='出力先ディレクトリパス（デフォルト: カレントディレクトリ）'
    )
    
    parser.add_argument(
        '--dpi',
        type=int,
        default=300,
        help='画像の解像度（DPI）（デフォルト: 300）'
    )
    
    args = parser.parse_args()
    
    try:
        # 入力ファイルの存在確認
        input_path = Path(args.input_pdf)
        if not input_path.exists():
            print(f"エラー: 入力ファイルが見つかりません: {args.input_pdf}", file=sys.stderr)
            sys.exit(1)
        
        if not input_path.is_file():
            print(f"エラー: 指定されたパスはファイルではありません: {args.input_pdf}", file=sys.stderr)
            sys.exit(1)
        
        # PDFファイルかどうかを拡張子で簡易チェック
        if input_path.suffix.lower() != '.pdf':
            print(f"警告: 入力ファイルの拡張子が.pdfではありません: {input_path.suffix}")
        
        print(f"PDFファイルを読み込み中: {args.input_pdf}")
        print(f"出力先ディレクトリ: {args.output}")
        print(f"解像度: {args.dpi} DPI")
        print()
        
        # PDF→画像変換を実行
        output_files = convert_pdf_to_images(args.input_pdf, args.output, args.dpi)
        
        # 結果を表示
        print()
        print(f"完了: {len(output_files)} 個の画像ファイルを生成しました")
        output_abs_path = Path(args.output).resolve()
        print(f"出力先: {output_abs_path}")
        
    except Exception as e:
        print(f"エラー: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
