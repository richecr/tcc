from pyxpdf import Document

from utils import write_txt


def extract_pyxpdf(pdf, uf):
    with open(pdf, 'rb') as fp:
        doc = Document(fp)
        filename = 'output_{}.txt'.format(pdf.split("/")[3])
        path_dir = "./outputs/pyxpdf_dou_{}/".format(uf)
        write_txt(
            doc.text(),
            filename=filename,
            dir=path_dir,
            mode="a"
        )
