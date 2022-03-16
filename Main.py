import fitz
from tcc.extract_text.pymupdf import init as pymupdf
from tcc.extract_text.pdfminer_six import init as pdfminer_six


pymupdf('./tcc/pdfs_samples/ac/dou_ac_17_12_21.pdf')


# pymupdf3('./tcc/pdfs_samples/ac/testes.pdf')
# pymupdf2('./tcc/pdfs_samples/ac/dou_ac_17_12_21.pdf')

# pymupdf('./tcc/pdfs_samples/ac/teste.pdf')


# pdfminer_six('x.pdf')

# pdf = fitz.open('./x.pdf')

# count = 1
# pages = []
# for page in pdf:
#     dict_page = page.get_text('text', flags=24)
#     pages.append(dict_page)
#     if count == 9:
#         break
#     count += 1

# print(pages)
