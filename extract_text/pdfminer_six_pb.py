import os
from extract_pdfminer_six import extract_pdfminer_six

caminhos = [os.path.join('./pdfs_samples/pb/', nome) for nome in os.listdir('./pdfs_samples/pb')]
arquivos = [arq for arq in caminhos if os.path.isfile(arq)]
pdfs = [arq for arq in arquivos if arq.lower().endswith(".pdf")]

print(pdfs)
for pdf in pdfs:
    extract_pdfminer_six(pdf)
