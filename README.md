# IMGtoPDF

画像ファイルとPDFファイルを相互に変換するPythonスクリプト集

## 機能

### img_to_pdf.py - 画像からPDFへの変換

- 指定したディレクトリ内の画像ファイル（.bmp/.jpg/.jpeg/.png/.tiff/.tif）を検索
- ファイル名の昇順でソート
- 1ページに1枚の画像を配置したPDFファイルを生成
- カレントディレクトリに指定したファイル名でPDFを出力

### pdf_to_img.py - PDFから画像への変換

- PDFファイルの各ページをPNG画像として出力
- ページごとに連番ファイル名（000.png, 001.png, ...）で保存
- 解像度（DPI）の指定が可能
- 指定したディレクトリまたはカレントディレクトリに出力

## 必要要件

- Python 3.6以上
- Pillow 10.2.0以上
- PyMuPDF 1.26.0以上（pdf_to_img.pyを使用する場合）

## インストール

```bash
pip install -r requirements.txt
```

## 使用方法

### img_to_pdf.py - 画像からPDFへの変換

#### 基本的な使い方

```bash
python img_to_pdf.py <画像ディレクトリのパス>
```

デフォルトでは`output.pdf`というファイル名で出力されます。

#### 出力ファイル名を指定する

```bash
python img_to_pdf.py <画像ディレクトリのパス> -o <出力ファイル名.pdf>
```

または

```bash
python img_to_pdf.py <画像ディレクトリのパス> --output <出力ファイル名.pdf>
```

#### 使用例

```bash
# デフォルトのファイル名（output.pdf）で出力
python img_to_pdf.py ./my_images

# カスタムファイル名で出力
python img_to_pdf.py ./my_images -o document.pdf

# 絶対パスも使用可能
python img_to_pdf.py /home/user/pictures --output scanned_document.pdf
```

### pdf_to_img.py - PDFから画像への変換

#### 基本的な使い方

```bash
python pdf_to_img.py <PDFファイルのパス>
```

カレントディレクトリに`000.png`、`001.png`...のような連番ファイル名で各ページが出力されます。

#### 出力先ディレクトリを指定する

```bash
python pdf_to_img.py <PDFファイルのパス> -o <出力ディレクトリパス>
```

または

```bash
python pdf_to_img.py <PDFファイルのパス> --output <出力ディレクトリパス>
```

#### 解像度（DPI）を指定する

```bash
python pdf_to_img.py <PDFファイルのパス> --dpi <解像度>
```

デフォルトは300 DPIです。値を小さくするとファイルサイズが小さくなりますが、画質が低下します。

#### 使用例

```bash
# カレントディレクトリに出力（デフォルト）
python pdf_to_img.py document.pdf

# 出力先ディレクトリを指定
python pdf_to_img.py document.pdf -o ./output_images

# 解像度を指定（150 DPI）
python pdf_to_img.py document.pdf --dpi 150

# 出力先と解像度を両方指定
python pdf_to_img.py document.pdf -o ./images --dpi 200
```

## サポートされる画像形式

### img_to_pdf.py

- BMP (.bmp)
- JPEG (.jpg, .jpeg)
- PNG (.png)
- TIFF (.tiff, .tif)

### pdf_to_img.py

- 出力形式: PNG (.png)

## 制限事項

### img_to_pdf.py

- 画像ファイルはファイル名の昇順（アルファベット順）でPDFに配置されます
- サブディレクトリ内の画像ファイルは処理されません（指定したディレクトリ直下のみ）
- 非常に大きな画像や大量の画像を処理する場合、メモリ使用量が増加する可能性があります
- 出力されるPDFの各ページサイズは、元の画像のサイズに依存します

### pdf_to_img.py

- 出力形式はPNGのみです
- 解像度（DPI）を高く設定すると、ファイルサイズが大きくなります
- 大量のページを含むPDFを変換する場合、処理時間とディスク容量に注意してください
- ファイル名は自動的に連番（000.png, 001.png, ...）で生成され、変更できません

## トラブルシューティング

### img_to_pdf.py

#### エラー: 対応する画像ファイルが見つかりませんでした

指定したディレクトリに対応形式の画像ファイルが存在しません。ディレクトリパスとファイル形式を確認してください。

#### エラー: ディレクトリが見つかりません

指定したパスが存在しないか、アクセス権限がありません。正しいパスを指定してください。

### pdf_to_img.py

#### エラー: 入力ファイルが見つかりません

指定したPDFファイルが存在しません。ファイルパスを確認してください。

#### エラー: PDFの読み込みに失敗する

ファイルが破損しているか、パスワードで保護されている可能性があります。別のPDFファイルで試してください。

## ライセンス

このプロジェクトはオープンソースです。
