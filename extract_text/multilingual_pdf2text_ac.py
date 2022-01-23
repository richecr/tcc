import os
import time
import logging
from os.path import exists
from extract_multilingual_pdf2text import extract_multilingual_ocr

directory = os.listdir('./pdfs_samples/ac')
paths = [os.path.join('./pdfs_samples/ac/', nome) for nome in directory]
files = [file for file in paths if os.path.isfile(file)]
pdfs = [pdf for pdf in files if pdf.lower().endswith(".pdf")]

logging.info("Iniciado extração de textos dos PDF")
print(pdfs)
logging.info("São um total de {} pdfs".format(len(pdfs)))


def extract(pdf):
    filename = pdf.split("/")[3]
    file_exists = exists("./outputs/multilingual_ocr_dou_ac/output_{}.txt".format(filename))
    if not file_exists:
        extract_multilingual_ocr(pdf, "ac")
        logging.info("Extração do pdf {} concluído".format(filename))
    else:
        logging.info("Extração do pdf {} já foi feita".format(filename))


start_time = time.time()
count = 1
for pdf in pdfs:
    extract(pdf)
    count += 1

print("--- %s seconds ---" % (time.time() - start_time))
