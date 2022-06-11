import fitz

from tcc.processing.main_extract import get_text_all
from tcc.extract_text.utils import write_json, write_txt


def filter_blocks(block):
    return (block['bbox'][0] <= 320 and block['bbox'][0] >= 319) or (
        block['bbox'][0] <= 54 and block['bbox'][0] >= 53
    )


def filter_entities(span):
    return (
        span['size'] == 9.895999908447266
        and (span['color'] == 2236191 or span['color'] == 16777215)
        and span['ascender'] == 0.9052734375
        and span['descender'] == -0.2119140625
    )


def lines2entities(lines):
    spans = []
    for line in lines:
        spans.extend(line['spans'])
    spans = list(filter(filter_entities, spans))
    return spans


def blocks2lines(blocks):
    lines = []
    for block in blocks:
        lines.extend(block['lines'])
    return lines


def get_rects_interested(page):
    paths = page.get_drawings()
    rects_interested = []
    colors_draw = [
        (0.13669031858444214, 0.12195010483264923, 0.1252918243408203),
        (0.5772945880889893, 0.5855344533920288, 0.5958037972450256),
        (0.6552987098693848, 0.6636301279067993, 0.6734569072723389),
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
            if p_color == colors_draw[3]:
                last = path
            if p_color in colors_draw[0:3]:
                rects_interested.append(path)
                page.draw_rect(path['rect'], color=(1, 0, 0))

    if last is not None:
        rects_interested.append(last)
        page.draw_rect(last['rect'], color=(1, 0, 0))
    return rects_interested


def get_text_from_page(page):
    dict_page = page.get_text('dict', flags=24)
    blocks = dict_page['blocks']
    return blocks


def init(path_file):
    pdf = fitz.open(path_file)

    count = 1
    result = ''
    entities = []
    for page in pdf:
        rects_interested = get_rects_interested(page)
        blocks = get_text_from_page(page)
        lines = blocks2lines(blocks)
        entities.extend(lines2entities(lines))
        lines.sort(
            key=lambda rect: (int(rect['bbox'][0]), int(rect['bbox'][1]))
        )
        lines = list(filter(filter_blocks, lines))
        if count == 1:
            res = get_text_all(lines, rects_interested, True)
        else:
            res = get_text_all(lines, rects_interested, False)

        if res != '':
            result += res
        # if count == 30:
        #     break
        count += 1

    pdf.ez_save('x.pdf')
    filename = path_file.split('/')[6].replace('pdf', 'txt')
    acts_entities = result.split('**************** ENTITY ****************')
    result_ = {}
    for i in range(len(entities)):
        if entities[i]['flags'] == 16:
            result_[entities[i]['text']] = {}
            for j in range(i + 1, len(entities)):
                if entities[j]['flags'] != 0:
                    break
                result_[entities[i]['text']][entities[j]['text']] = []

    for act, key_ent in zip(acts_entities[1:], result_.keys()):
        acts_title = act.split('**************** TITLE ****************')
        if "**************** TITLE ****************" not in act:
            acts = list(
                filter(
                    lambda x: x != '', acts_title[0].split('\n\n------\n\n')
                )
            )
            result_[key_ent] = acts
        else:
            acts_title = acts_title[1:]
            for acts, key_title in zip(acts_title, result_[key_ent]):
                acts = list(
                    filter(lambda x: x != '', acts.split('\n\n------\n\n'))
                )
                result_[key_ent][key_title] = acts

    write_json(
        result_,
        filename=filename.replace('txt', 'json'),
        dir='./tcc/outputs/json/2021/08/',
    )
    # write_txt(result, filename=filename)
    print('${filename}: Concluido!'.format(filename=filename))
