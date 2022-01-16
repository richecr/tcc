from io import StringIO

from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser

from utils import write_txt_pb


def extract_pdfminer_six(pdf, uf):
    output_string = StringIO()
    with open(pdf, 'rb') as in_file:
        parser = PDFParser(in_file)
        doc = PDFDocument(parser)
        rsrcmgr = PDFResourceManager()
        device = TextConverter(
            rsrcmgr, output_string, codec="utf-8", laparams=LAParams())
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        for page in PDFPage.create_pages(doc):
            interpreter.process_page(page)

    content = output_string.getvalue()
    device.close()
    output_string.close()
    content = content.replace("�", '.')
    filename = 'output_{}.txt'.format(pdf.split("/")[3])
    path_dir = "./outputs/pdfminer_six_dou_{}/".format(uf)
    write_txt_pb(
        content, filename=filename, dir=path_dir)
