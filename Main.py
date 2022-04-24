from tcc.extract_text.pymupdf import init as pymupdf
from tcc.extract_text.pdfminer_six import init as pdfminer_six

pdfs = [
    './tcc/pdfs_samples/ac/dou_ac_17_12_21.pdf',
    './tcc/pdfs_samples/ac/dou_ac_20_12_21.pdf',
    './tcc/pdfs_samples/ac/dou_ac_21_12_21.pdf',
    './tcc/pdfs_samples/ac/dou_ac_22_12_21.pdf',
    './tcc/pdfs_samples/ac/dou_ac_23_12_21.pdf',
]

for pdf in pdfs:
    try:
        pymupdf(pdf)
    except Exception as ex:
        print(f'{pdf} falhou: {ex=}')

# pymupdf('./tcc/pdfs_samples/ac/dou_ac_22_12_21.pdf')


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
