import json
import fitz

from utils import write_json

pdf = fitz.open('./pdfs_samples/ac/dou_ac_17_12_21.pdf')

count = 1
pages = []
for page in pdf:
    if count == 9:
        dict_page = page.get_text("dict", flags=24)
        text_page = json.dumps(dict_page)
        text_page = text_page.replace("�", '.')
        dict_page = json.loads(text_page)
        pages.append(dict_page)
        break
    else:
        count += 1

write_json(pages, filename="data_pymupdf.json")
