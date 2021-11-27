import fitz

from utils import write_json, write_txt

pdf = fitz.open('./pdfs_samples/page1.pdf')
for page in pdf:
    text = page.get_text("dict")
    # blocos tem informações mais detalhadas sobre cada linha do PDF.
    # talvez não seja útil para deixar a solução genérica, mas seria útil 
    # para pegar as ente do documento. 
    for b in text['blocks']:
        print(b)
        print("\n\n")

    # write_json(text, filename="data_pymupdf.json")

    text = page.get_text("html")
    write_txt(text, filename='index_pymupdf.html')

    text = page.get_text()
    write_txt(text, filename='output_pymupdf.txt')