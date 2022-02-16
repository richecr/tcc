import json
import fitz

from utils import write_json

pdf = fitz.open('./pdfs_samples/ac/dou_ac_17_12_21.pdf')

count = 1
pages = []
for page in pdf:
    paths = page.get_cdrawings()
    rects_interested = []
    for path in paths:
        if path['type'] == 's' and len(path['items']) == 1:
            if path['color'] == (0.13669031858444214, 0.12195010483264923, 0.1252918243408203):
                page.draw_rect(path["rect"], color=(1, 0, 0))
                rects_interested.append(path)

    dict_page = page.get_text("dict", flags=24)
    text_page = json.dumps(dict_page)
    text_page = text_page.replace("�", '.')
    dict_page = json.loads(text_page)
    pages.append(dict_page)

pdf.ez_save("x.pdf")

write_json(pages, filename="data_pymupdf.json")
