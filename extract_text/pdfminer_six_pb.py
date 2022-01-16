import os
from extract_pdfminer_six import extract_pdfminer_six

directory = os.listdir('./pdfs_samples/pb')
caminhos = [os.path.join('./pdfs_samples/pb/', nome) for nome in directory]
arquivos = [arq for arq in caminhos if os.path.isfile(arq)]
pdfs = [arq for arq in arquivos if arq.lower().endswith(".pdf")]

print("Iniciado extração de textos dos PDF")
print(pdfs)
print("São um total de {} pdfs".format(len(pdfs)))

count = 1
for pdf in pdfs:
    extract_pdfminer_six(pdf, "pb")
    filename = pdf.split("/")[3]
    print("Extração do pdf {} - {} concluído".format(count, filename))
    count += 1
