import json
from sys import flags
import fitz
from numpy import block

from tcc.processing.main_subtext_pymupdf import get_all, concat_texts_blocks2

from .utils import write_json, write_txt


def filter_blocks(block):
    return (
        (block['bbox'][0] <= 320 and block['bbox'][0] >= 319)
        or (block['bbox'][0] <= 54 and block['bbox'][0] >= 53)
    )


def init(path_file):
    pdf = fitz.open(path_file)

    count = 1
    pages = []
    result = ''
    for page in pdf:
        paths = page.get_drawings()
        rects_interested = []
        colors_draw = [
            (0.13669031858444214, 0.12195010483264923, 0.1252918243408203),
            (0.5772945880889893, 0.5855344533920288, 0.5958037972450256),
            (0.3449302017688751, 0.3479514718055725, 0.35645076632499695),
        ]
        last = None
        for path in paths:
            if (
                path['type'] == 's'
                and (len(path['items']) == 1)
                and path['width'] != 0.25
            ):
                p_color = path['color']
                if p_color == colors_draw[2]:
                    last = path
                if p_color in colors_draw[0:2]:
                    rects_interested.append(path)
                    page.draw_rect(path['rect'], color=(1, 0, 0))

        if last is not None:
            rects_interested.append(last)
            page.draw_rect(last['rect'], color=(1, 0, 0))

        dict_page = page.get_text('dict', flags=24)
        pages.append(dict_page)
        blocks = dict_page['blocks']
        if count != 1:
            blocks.sort(key=lambda rect: (rect['bbox'][0], rect['bbox'][1]))
        blocks = list(filter(filter_blocks, blocks))
        # rects_interested.sort(key=lambda rect: rect['rect'][1])
        if count == 23:
            print("OPA")
        res = get_all(blocks, rects_interested)
        if res != '':
            result += res
        if count == 27:
            break
        count += 1

    pdf.ez_save('x.pdf')
    # write_json(pages, filename='data_pymupdf.json')
    filename = path_file.split("/")[4].replace("pdf", "txt")
    write_txt(result, filename=filename)
