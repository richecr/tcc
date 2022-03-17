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
        if (rect_start[0] <= 57 and rect_start[0] >= 53) and (
            rect_end[0] <= 320 and rect_end[0] >= 319
        ):
            if block['bbox'][0] >= 53 and block['bbox'][0] <= 54.4:
                if block['bbox'][1] >= rect_start[1]:
                    result += concatena_lines(block)
            elif block['bbox'][0] >= 319 and block['bbox'][0] <= 320:
                if block['bbox'][1] <= rect_end[1]:
                    result += concatena_lines(block)
        elif (
            block['bbox'][1] >= rect_start[1]
            and block['bbox'][1] <= rect_end[1]
        ):
            if (rect_start[0] >= 53 and rect_start[0] <= 57):
                if block['bbox'][0] >= 53 and block['bbox'][0] <= 54.4:
                    result += concatena_lines(block)
            else:
                if block['bbox'][0] >= 319 and block['bbox'][0] <= 320:
                    result += concatena_lines(block)
        # if (
        #     block['bbox'][1] >= rect_start[1]
        #     and block['bbox'][1] <= rect_end[1]
        # ):
        #     result += concatena_lines(block)

    return result


def get_first_block(blocks, rect_start):
    for block in blocks:
        if rect_start[0] <= 57 and rect_start[0] >= 53:
            if block['bbox'][0] >= 53 and block['bbox'][0] <= 54.4:
                if block['bbox'][1] >= rect_start[1]:
                    return block
        elif block['bbox'][1] >= rect_start[1]:
            if rect_start[0] >= 53 and rect_start[0] <= 54.4:
                if block['bbox'][0] >= 53 and block['bbox'][0] <= 54.4:
                    return block
    return None


def get_last_block(blocks, rect_start, rect_end):
    result = ''
    for block in blocks:
        if (rect_start[0] <= 57 and rect_start[0] >= 53) and (
            rect_end[0] <= 320 and rect_end[0] >= 319
        ):
            if block['bbox'][0] >= 53 and block['bbox'][0] <= 54.4:
                if block['bbox'][1] >= rect_start[1]:
                    result = block
            elif block['bbox'][0] >= 319 and block['bbox'][0] <= 320:
                if block['bbox'][1] <= rect_end[1]:
                    result = block
        elif (
            block['bbox'][1] >= rect_start[1]
            and block['bbox'][1] <= rect_end[1]
        ):
            if (rect_start[0] >= 53 and rect_start[0] <= 54.4):
                if block['bbox'][0] >= 53 and block['bbox'][0] <= 54.4:
                    result = block
            else:
                if block['bbox'][0] >= 319 and block['bbox'][0] <= 320:
                    result = block
    return result


def concat_test(blocks, rect_start, rect_end):
    result = ''
    for block in blocks:
        if (
            block['bbox'][1] >= rect_start[1]
            and block['bbox'][1] <= rect_end[1]
        ):
            result += concatena_lines(block)
    return result


def is_start_publish(blocks):
    if len(blocks) > 0:
        first_block = blocks[0]
        text_line = concatena_spans(first_block['lines'][0])
        if text_line.isupper() and not text_line[0].isdigit():
            return True
    return False

def get_all(blocks, rects_interested):
    result = ''
    end_ = (0.3449302017688751, 0.3479514718055725, 0.35645076632499695)
    if is_start_publish(blocks):
        result += '\n\n------\n\n'
    if len(rects_interested) == 2:
        result += concat_test(
            blocks=blocks,
            rect_start=rects_interested[0]['rect'],
            rect_end=rects_interested[1]['rect']
        )
    else:
        for i in range(0, len(rects_interested) - 1, 1):
            res = concat_texts_blocks(
                blocks=blocks,
                rect_start=rects_interested[i]['rect'],
                rect_end=rects_interested[i + 1]['rect'],
            )
            if res != '' and res != ' ':
                if (
                    rects_interested[i]['color'] == end_
                    or rects_interested[i + 1]['color'] == end_
                ):
                    result += res
                else:
                    result += res
                    result += '\n\n------\n\n'

    result = result.replace('�', '.')
    return result


def concat_texts_blocks2(blocks):
    result = ''
    for block in blocks:
        result += concatena_lines(block)

    return result
