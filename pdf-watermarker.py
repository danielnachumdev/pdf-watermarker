from logging import error
import img2pdf
import PyPDF2
from sys import argv
from fpdf import FPDF
import os
from local_vars import DEFAULT_WATERMARK_PATH
INPUT_INDEX = 1
OUTPUT_INDEX = 2
WATERMARK_FILE_INPUT_INDEX = 3
DESKTOP_PATH = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
TMP_PDF = "temporary_file_671823476598176591.pdf"
DEFUALT_OUTPUT_NAME = "output.pdf"


def apply_watermark(pdf_file, output_file, watermark):
    def picture_to_pdf(path: str) -> PyPDF2.PdfFileReader:
        with open(TMP_PDF, "wb") as f:
            f.write(img2pdf.convert(path))
            return PyPDF2.PdfFileReader(TMP_PDF)

    def delete_file(path):
        os.remove(path)

    watermark_file = open(watermark, 'rb')
    watermark_page = picture_to_pdf(watermark).getPage(0)
    input_file = open(pdf_file, 'rb')
    input_pdf = PyPDF2.PdfFileReader(input_file)
    output = PyPDF2.PdfFileWriter()
    result = open(output_file, 'wb')
    for i in range(input_pdf.numPages):
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
    if not os.path.exists(pdf_file):
        error(f"File \"{pdf_file}\" does not exist")
        return False
    if not os.path.exists(watermark):
        error(f"File \"{watermark}\" does not exist")
        return False
    elif os.path.exists(output_file):
        error(f"File \"{output_file}\" already exists")
        return False
    return True


def parse_input(argv):
    pdf_file = argv[INPUT_INDEX]
    watermark = DEFAULT_WATERMARK_PATH
    output_file = DESKTOP_PATH+"//"+DEFUALT_OUTPUT_NAME
    if len(argv) >= 3:
        watermark = argv[WATERMARK_FILE_INPUT_INDEX]
    if (len(argv) >= 4):
        output_file = argv[OUTPUT_INDEX]
    return pdf_file, output_file, watermark


if __name__ == '__main__':
    if len(argv) >= 2:
        pdf_file, output_file, watermark = parse_input(argv)
        if is_input_valid(pdf_file, output_file, watermark):
            apply_watermark(pdf_file, output_file, watermark)
    else:
        print(
            "Usage: python pdf-watermarker.py [pdf_file] ?[output_file] ?[watermark_file]")
