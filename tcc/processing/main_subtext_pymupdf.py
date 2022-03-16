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


def get_all(blocks, rects_interested):
    result = ''
    end_ = (0.3449302017688751, 0.3479514718055725, 0.35645076632499695)
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
                    block = get_last_block(
                        blocks,
                        rects_interested[i]['rect'],
                        rects_interested[i + 1]['rect'],
                    )
                    try:
                        if len(block['lines']) in [1, 2, 3]:
                            result += res
                            result += '\n\n------\n\n'
                        else:
                            result += res
                    except Exception as ex:
                        result += res
                        result += '\n\n------\n\n'
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
