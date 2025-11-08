# IMGtoPDF

フォルダに格納された画像ファイルを一個のPDFファイルにまとめるPythonスクリプト

## 機能

- 指定したディレクトリ内の画像ファイル（.bmp/.jpg/.jpeg/.png/.tiff/.tif）を検索
- ファイル名の昇順でソート
- 1ページに1枚の画像を配置したPDFファイルを生成
- カレントディレクトリに指定したファイル名でPDFを出力

## 必要要件

- Python 3.6以上
- Pillow 10.2.0以上

## インストール

```bash
pip install -r requirements.txt
```

## 使用方法

### 基本的な使い方

```bash
python img_to_pdf.py <画像ディレクトリのパス>
```

デフォルトでは`output.pdf`というファイル名で出力されます。

### 出力ファイル名を指定する

```bash
python img_to_pdf.py <画像ディレクトリのパス> -o <出力ファイル名.pdf>
```

または

```bash
python img_to_pdf.py <画像ディレクトリのパス> --output <出力ファイル名.pdf>
```

### 使用例

```bash
# デフォルトのファイル名（output.pdf）で出力
python img_to_pdf.py ./my_images

# カスタムファイル名で出力
python img_to_pdf.py ./my_images -o document.pdf

# 絶対パスも使用可能
python img_to_pdf.py /home/user/pictures --output scanned_document.pdf
```

## サポートされる画像形式

- BMP (.bmp)
- JPEG (.jpg, .jpeg)
- PNG (.png)
- TIFF (.tiff, .tif)

## 制限事項

- 画像ファイルはファイル名の昇順（アルファベット順）でPDFに配置されます
- サブディレクトリ内の画像ファイルは処理されません（指定したディレクトリ直下のみ）
- 非常に大きな画像や大量の画像を処理する場合、メモリ使用量が増加する可能性があります
- 出力されるPDFの各ページサイズは、元の画像のサイズに依存します

## トラブルシューティング

### エラー: 対応する画像ファイルが見つかりませんでした

指定したディレクトリに対応形式の画像ファイルが存在しません。ディレクトリパスとファイル形式を確認してください。

### エラー: ディレクトリが見つかりません

指定したパスが存在しないか、アクセス権限がありません。正しいパスを指定してください。

## ライセンス

このプロジェクトはオープンソースです。
