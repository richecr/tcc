import logging
import os
from extract_multilingual_pdf2text import extract_multilingual_ocr

directory = os.listdir('./pdfs_samples/pb')
paths = [os.path.join('./pdfs_samples/pb/', nome) for nome in directory]
files = [file for file in paths if os.path.isfile(file)]
pdfs = [pdf for pdf in files if pdf.lower().endswith(".pdf")]

logging.info("Iniciado extração de textos dos PDF")
print(pdfs)
logging.info("São um total de {} pdfs".format(len(pdfs)))
count = 1

for pdf in pdfs:
    extract_multilingual_ocr(pdf, "pb")
    filename = pdf.split("/")[3]
    logging.info("Extração do pdf {} - {} concluído".format(count, filename))
    count += 1
