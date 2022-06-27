import os

from tcc.extract_text.pymupdf import init as pymupdf

dir = './tcc/pdfs_samples/ac/2021/11/'
directory = os.listdir(dir)
pdfs = [os.path.join(dir, nome) for nome in directory]

# pdfs = [
#     './tcc/pdfs_samples/ac/2021/10/dou_ac_08_10_21.pdf',
# ]

for pdf in pdfs:
    try:
        pymupdf(pdf, './tcc/outputs/json/2021/11/')
    except Exception as ex:
        print(f'{pdf} falhou: {ex=}')
