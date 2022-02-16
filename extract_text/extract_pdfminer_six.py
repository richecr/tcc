from ctypes import cast
from io import StringIO
from typing import Dict, Iterable, Iterator, List, Optional, Tuple

from pdfminer.utils import apply_matrix_pt, Matrix, Rect, fsplit, Plane, uniq
from pdfminer.converter import PDFConverter, TextConverter
from pdfminer.layout import (
    LAParams,
    LTPage,
    LTTextBox,
    LTChar,
    LTFigure,
    LTTextLine,
    LTTextBoxVertical,
    LTLayoutContainer,
    LTTextBoxHorizontal,
    LTTextLineHorizontal,
    LTTextLineVertical,
    LTComponent,
    IndexAssigner
)
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser, PDFStreamParser

from utils import write_txt_pb


def extract_pdfminer_six(pdf, uf):
    output_string = StringIO()
    with open(pdf, 'rb') as in_file:
        parser = PDFParser(in_file)
        doc = PDFDocument(parser)
        rsrcmgr = PDFResourceManager()
        device = TextConverter(
            rsrcmgr, output_string, codec="utf-8",
            laparams=LAParams())
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        for page in PDFPage.create_pages(doc):
            interpreter.process_page(page)

    content = output_string.getvalue()
    device.close()
    output_string.close()
    content = content.replace("�", '.')
    filename = 'output_{}.txt'.format("teste")
    path_dir = "./outputs/pdfminer_six_dou_{}_2/".format(uf)
    print("AQUI")
    c = ""
    for a in content.split("ESTADO DO ACRE\n"):
        c += a
        c += "\n\n++++++++++++++++++++++++++++++++++++++\n\n"

    write_txt_pb(
        c, filename=filename, dir=path_dir)
