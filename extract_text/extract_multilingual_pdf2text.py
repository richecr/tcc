import logging
import pytesseract
from multilingual_pdf2text.pdf2text import PDF2Text
from multilingual_pdf2text.models.document_model.document import Document

from utils import write_txt

logging.basicConfig(level=logging.INFO)
# path_tesseract_ocr = r'D:\Programas\Tesseract-OCR\tesseract.exe'
# pytesseract.pytesseract.tesseract_cmd = path_tesseract_ocr


def extract_multilingual_ocr(pdf):
    pdf_document = Document(document_path=pdf, language="por")
    pdf2text = PDF2Text(document=pdf_document)
    content = pdf2text.extract()
    for page in content:
        filename = 'output_{}.txt'.format(pdf.split("/")[3])
        write_txt(
            page["text"],
            filename=filename,
            dir="./outputs/multilingual_ocr_dou_pb/",
            mode="a"
        )
