from multilingual_pdf2text.pdf2text import PDF2Text
from multilingual_pdf2text.models.document_model.document import Document
import pytesseract
import logging

from utils import write_txt

logging.basicConfig(level=logging.INFO)

pytesseract.pytesseract.tesseract_cmd = r'D:\Programas\Tesseract-OCR\tesseract.exe'

def main():
    pdf_document = Document(
        document_path="./pdfs_samples/pb/dou_pb_17_12_21.pdf",
        language="por"
    )
    pdf2text = PDF2Text(document=pdf_document)
    content = pdf2text.extract()
    for page in content:
        print(page["text"])
        write_txt(page["text"], filename="output_multilingual_pdf2_pb.txt", mode="a")



if __name__ == "__main__":
    main()
