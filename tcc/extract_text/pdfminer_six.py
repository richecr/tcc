from io import StringIO
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser

from tcc.extract_text.utils import write_txt


def init(pdf):
    output_string = StringIO()
    with open(pdf, 'rb') as in_file:
        parser = PDFParser(in_file)
        doc = PDFDocument(parser)
        rsrcmgr = PDFResourceManager()
        device = TextConverter(rsrcmgr, output_string, laparams=LAParams())
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        count = 1
        for page in PDFPage.create_pages(doc):
            interpreter.process_page(page)
            if count == 9:
                break
            count += 1
    res = output_string.getvalue()
    res = res.replace('�', '.')
    write_txt(res, 'test_pdfminer.txt')
