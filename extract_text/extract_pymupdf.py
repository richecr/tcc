import json
import fitz

from utils import write_json, write_txt

pdf = fitz.open('./pdfs_samples/ac/dou_ac_17_12_21.pdf')

count = 1
for page in pdf:
    # Pode ser usado o método de OCR.
    # text = page.get_textpage_ocr(flags=88)

    text = page.get_text("dict", flags=88)
    # blocos tem informações mais detalhadas sobre cada linha do PDF.
    # talvez não seja útil para deixar a solução genérica, mas seria útil
    # para pegar as ente do documento.
    # for block in text['blocks']:
    #     print(block)
    #     print("\n")
    #     # try:
    #     #     for line in block['lines']:
    #     #         if line['spans'][0]['font'] == 'ArialMT' and line['spans'][0]['size'] == 9.895999908447266:
    #     #             print(block)
    #     # except Exception:
    #     #     continue

    write_json(text, filename="data_pymupdf.json")

    text = page.get_text("html")
    write_txt(text, filename='index_pymupdf.html')

    text = page.get_text()
    text = text.replace("�", '.')
    write_txt(text, filename='output_pymupdf.txt')
    if count == 1:
        break
    count += 1
