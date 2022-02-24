import json
import fitz

from tcc.processing.main_subtext_pymupdf import get_all

from .utils import write_json, write_txt


def init(path):
    pdf = fitz.open(path)

    count = 1
    pages = []
    result = ''
    for page in pdf:
        paths = page.get_cdrawings()
        rects_interested = []
        colors_draw = [
            (0.13669031858444214, 0.12195010483264923, 0.1252918243408203),
            (0.5772945880889893, 0.5855344533920288, 0.5958037972450256),
            (0.3449302017688751, 0.3479514718055725, 0.35645076632499695),
        ]
        for path in paths:
            if (
                path['type'] == 's'
                and (len(path['items']) == 1)
                and path['width'] != 0.25
            ):
                p_color = path['color']
                if p_color in colors_draw:
                    rects_interested.append(path)
                    page.draw_rect(path['rect'], color=(1, 0, 0))

        dict_page = page.get_text('dict', flags=24)
        pages.append(dict_page)
        rects_interested.sort(key=lambda rect: rect['rect'][1])
        res = get_all(dict_page['blocks'], rects_interested)
        if res != '':
            result += res
        if count == 6:
            break
        count += 1

    pdf.ez_save('x.pdf')
    # write_json(pages, filename='data_pymupdf.json')
    write_txt(result, filename='test.txt')
