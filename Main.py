import os

from tcc.extract_text.pymupdf import init as pymupdf

dir = './tcc/pdfs_samples/ac/2021/08/'
directory = os.listdir(dir)
pdfs = [os.path.join(dir, nome) for nome in directory]

# pdfs = [
#     './tcc/pdfs_samples/ac/dou_ac_17_12_21.pdf',
#     './tcc/pdfs_samples/ac/dou_ac_20_12_21.pdf',
#     './tcc/pdfs_samples/ac/dou_ac_21_12_21.pdf',
#     './tcc/pdfs_samples/ac/dou_ac_22_12_21.pdf',
#     './tcc/pdfs_samples/ac/dou_ac_23_12_21.pdf',
# ]

for pdf in pdfs:
    try:
        pymupdf(pdf)
    except Exception as ex:
        print(f'{pdf} falhou: {ex=}')
