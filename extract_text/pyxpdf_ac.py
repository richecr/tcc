import os
import time
from extract_pyxpdf import extract_pyxpdf

directory = os.listdir('./pdfs_samples/ac')
caminhos = [os.path.join('./pdfs_samples/ac/', nome) for nome in directory]
arquivos = [arq for arq in caminhos if os.path.isfile(arq)]
pdfs = [arq for arq in arquivos if arq.lower().endswith(".pdf")]

print("Iniciado extração de textos dos PDF")
print(pdfs)
print("São um total de {} pdfs".format(len(pdfs)))

start_time = time.time()
count = 1
for pdf in pdfs:
    extract_pyxpdf(pdf, "ac")
    filename = pdf.split("/")[3]
    print("Extração do pdf {} - {} concluído".format(count, filename))
    count += 1

print("--- %s seconds ---" % (time.time() - start_time))
# --- 565.4852545261383 ---
