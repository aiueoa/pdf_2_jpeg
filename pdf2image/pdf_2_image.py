# パッケージのインポート
import os
import glob
from pathlib import Path
from pdf2image import convert_from_path

def pdf_image(pdf_file,img_path, fmt='jpeg', dpi=200):

    #pdf_file、img_pathをPathにする
    pdf_path = Path(pdf_file)
    image_dir = Path(img_path)

    # PDFをImage に変換(pdf2imageの関数)
    pages = convert_from_path(pdf_path, dpi)

    # 画像ファイルを１ページずつ保存
    for i, page in enumerate(pages):
        file_name = "{}_{:02d}.{}".format(pdf_path.stem,i+1,fmt)
        image_path = image_dir / file_name
        page.save(image_path, fmt)

if __name__ == "__main__":
    path = os.getcwd()
    files = glob.glob(path+'/input/*')
    input_file = files[0]
    output_path = path+'/output'
    # PDFファイルのパス
    pdf_path = Path(input_file)
    img_path=Path(output_path)

    pdf_image(pdf_file=pdf_path,img_path=img_path, fmt='jpeg', dpi=200)