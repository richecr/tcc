from io import StringIO
import shutil

from pdfminer3.converter import TextConverter
from pdfminer3.layout import LAParams
from pdfminer3.pdfdocument import PDFDocument
from pdfminer3.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer3.pdfpage import PDFPage
from pdfminer3.pdfparser import PDFParser

from utils import write_txt

output_string = StringIO()
with open('./pdfs_samples/pdf_pb.pdf', 'rb') as in_file:
    parser = PDFParser(in_file)
    doc = PDFDocument(parser)
    rsrcmgr = PDFResourceManager()
    device = TextConverter(rsrcmgr, output_string, codec="utf-8", laparams=LAParams())
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    for page in PDFPage.create_pages(doc):
        interpreter.process_page(page)

content = output_string.getvalue()
device.close()
output_string.close()

content = content.replace("�", '.')

write_txt(content, filename='output_pdfminer3_pb.txt')
print(content)

