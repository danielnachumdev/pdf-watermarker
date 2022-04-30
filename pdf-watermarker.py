from logging import error
import img2pdf
import PyPDF2
from sys import argv
import os
from typing import Tuple
from local_vars import DEFAULT_WATERMARK_PATH
DEFAULT_PDF_INDEX = 1
DEFAULT_OUTPUT_INDEX = 2
DEFUALT_OUTPUT_NAME = "output.pdf"
DEFAULT_WATERMARK_INDEX = 3
DESKTOP_PATH = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
TMP_PDF = "temporary_file_671823476598176591.pdf"


def apply_watermark(pdf_path: str, output_path: str, watermark_path: str) -> None:
    def picture_to_pdf(path: str) -> PyPDF2.PdfFileReader:
        with open(TMP_PDF, "wb") as f:
            f.write(img2pdf.convert(path))
            return PyPDF2.PdfFileReader(TMP_PDF)

    def delete_file(path: str) -> None:
        os.remove(path)

    watermark_file = open(watermark_path, 'rb')
    watermark_page = picture_to_pdf(watermark_path).getPage(0)
    input_file = open(pdf_path, 'rb')
    input_pdf = PyPDF2.PdfFileReader(input_file)
    output = PyPDF2.PdfFileWriter()
    result = open(output_path, 'wb')
    for i in range(input_pdf.numPages):
        print(f"Page {i+1} / {input_pdf.numPages}")
        page = input_pdf.getPage(i)
        page.mergePage(watermark_page,)
        output.addPage(page)
        output.write(result)
    result.close()
    watermark_file.close()
    input_file.close()
    delete_file(TMP_PDF)
    print("Finished!")


def is_input_valid(pdf_file, output_file, watermark):
    def is_file_type(path: str, ext: str):
        return path.endswith(ext)
    if not os.path.exists(pdf_file):
        error(f"File \"{pdf_file}\" does not exist")
        return False
    if not os.path.exists(watermark):
        error(f"File \"{watermark}\" does not exist")
        return False
    if not is_file_type(watermark, ".png"):
        error(f"Watermark file must be a png file")
        return False
    elif os.path.exists(output_file):
        error(f"File \"{output_file}\" already exists")
        return False
    return True


def parse_input(argv: list[str]) -> Tuple[str, str, str]:
    pdf_file = argv[DEFAULT_PDF_INDEX]
    watermark = DEFAULT_WATERMARK_PATH
    output_file = DESKTOP_PATH+"//"+DEFUALT_OUTPUT_NAME
    if len(argv) >= 3:
        watermark = argv[DEFAULT_WATERMARK_INDEX]
    if (len(argv) >= 4):
        output_file = argv[DEFAULT_OUTPUT_INDEX]
    return pdf_file, output_file, watermark


if __name__ == '__main__':
    if len(argv) >= 2:
        pdf_file, output_file, watermark = parse_input(argv)
        if is_input_valid(pdf_file, output_file, watermark):
            apply_watermark(pdf_file, output_file, watermark)
    else:
        print(
            "Usage: python pdf-watermarker.py [pdf_file] ?[output_file] ?[watermark_file]")
