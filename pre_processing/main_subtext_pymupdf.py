import json


def calculate_distance_blocks(block1, block2):
    return block2['bbox'][1] - block1['bbox'][3]


def concatena_spans(line):
    spans = line['spans']
    paragraph = ""
    for span in spans:
        if not (span['font'] == 'Arial-BoldMT' or span['font'] == "TimesNewRomanPSMT" or span['color'] == 13750996 or span['color'] == 16777215 or span['size'] == 9.895999908447266):
            paragraph += span['text']
    return paragraph


def concatena_lines(block):
    lines = block['lines']
    paragraph = ""
    for line in lines:
        paragraph += concatena_spans(line) + " "
    return paragraph


def not_is_title(block):
    not_is = True
    for line in block['lines']:
        for span in line['spans']:
            if span['size'] == 9.895999908447266:
                not_is = False
                break

    return not_is

with open('./outputs/data_pymupdf.json', mode="r") as json_file:
    pages = json.loads(json_file.read())

    sub_texts = []
    for page in pages:
        blocks = page['blocks']
        sub_text = ''
        for i in range(0, len(blocks) - 1):
            if (calculate_distance_blocks(blocks[i], blocks[i+1]) <= 12
                    and not_is_title(blocks[i])):
                sub_text += concatena_lines(blocks[i])
            else:
                if sub_text != "":
                    sub_texts.append(sub_text.strip())
                    sub_text = ""

    text = ""
    for sub in sub_texts:
        text += sub + "\n\n\n------------------"

    file = "./outputs/output.txt"
    with open(file, mode="w", encoding="utf-8") as f:
        f.write(text)
