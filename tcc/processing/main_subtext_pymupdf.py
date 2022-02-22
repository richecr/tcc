def concatena_spans(line):
    spans = line['spans']
    paragraph = ''
    for span in spans:
        if not (
            span['font'] == 'Arial-BoldMT'
            or span['font'] == 'TimesNewRomanPSMT'
            or span['color'] == 13750996
            or span['color'] == 16777215
            or span['size'] == 9.895999908447266
        ):
            paragraph += span['text']
    return paragraph


def concatena_lines(block):
    lines = block['lines']
    paragraph = ''
    for line in lines:
        paragraph += concatena_spans(line) + ' '
    return paragraph


def concat_texts_blocks(blocks, rect_start, rect_end):
    result = ''
    for block in blocks:
        if (
            block['bbox'][1] <= rect_end[1]
            and block['bbox'][1] >= rect_start[1]
        ):
            result += concatena_lines(block)
    return result


def get_all(blocks, rects_interested):
    result = ''
    for i in range(0, len(rects_interested) - 1, 1):
        result += concat_texts_blocks(
            blocks=blocks,
            rect_start=rects_interested[i]['rect'],
            rect_end=rects_interested[i + 1]['rect'],
        )
        result += '\n\n------\n\n'
    result = result.replace('�', '.')
    return result
