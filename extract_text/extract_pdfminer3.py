from io import StringIO

from pdfminer3.converter import TextConverter
from pdfminer3.layout import LAParams
from pdfminer3.pdfdocument import PDFDocument
from pdfminer3.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer3.pdfpage import PDFPage
from pdfminer3.pdfparser import PDFParser

from utils import write_txt

output_string = StringIO()
with open('./pdfs_samples/page1.pdf', 'rb') as in_file:
    parser = PDFParser(in_file)
    doc = PDFDocument(parser)
    rsrcmgr = PDFResourceManager()
    device = TextConverter(rsrcmgr, output_string, laparams=LAParams())
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    for page in PDFPage.create_pages(doc):
        interpreter.process_page(page)

content = output_string.getvalue()
write_txt(content, filename='output_pdfminer3.txt')
print(content)