import re


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


def concatena_lines(line):
    paragraph = ''
    paragraph += concatena_spans(line) + ' '
    return paragraph


def concat_page_complete(blocks, rect_start, rect_end):
    result = ''
    for block in blocks:
        if (
            block['bbox'][1] >= rect_start[1]
            and block['bbox'][1] <= rect_end[1]
        ):
            result += concatena_lines(block)
    return result


def pre_processing(text: str):
    result: str = re.sub(r'º|ª|°|/', '', text)
    result: str = re.sub(r':|–', 'error', result)
    return result


def is_start_publish(lines):
    if len(lines) > 0:
        first_block = lines[0]
        text_line = concatena_spans(first_block)
        if (
            len(first_block['spans']) > 1
            or len(text_line.split(' ')) <= 2
            or len(text_line.split(' ')[0]) < 4
        ):
            return False

        text_line = pre_processing(text_line)
        if text_line.isupper() and not text_line[0].isdigit():
            return True
    return False


def line_is_start_publish(line):
    text_line = concatena_spans(line)
    if (
        len(line['spans']) > 1
        or len(text_line.split(' ')) <= 2
        or len(text_line.split(' ')[0]) < 4
    ):
        return False

    text_line = pre_processing(text_line)
    if (
        text_line.isupper()
        and not text_line[0].isdigit()
        and '�' not in text_line
    ):
        return True
    return False


def concat_texts_blocks(lines, rect_start, rect_end):
    result = ''
    two_col = 1
    test = False
    for line in lines:
        if (rect_start[0] <= 57 and rect_start[0] >= 53) and (
            rect_end[0] <= 322.2 and rect_end[0] >= 319
        ):
            if line['bbox'][0] >= 53 and line['bbox'][0] <= 54.4:
                # Página de duas colunas: Se for no final da primeira coluna,
                # da esquerda, então quer dizer que o próximo será a primeira
                # linha da coluna a direita.
                if two_col == 1:
                    two_col = 2
                if line['bbox'][1] >= rect_start[1]:
                    result += concatena_lines(line)
            elif line['bbox'][0] >= 319 and line['bbox'][0] <= 322.2:
                # Página de duas colunas: A última linha a ser lida foi a
                # última da coluna a esquerda, temos que verificar se aqui
                # não inicia um novo ato.
                if two_col == 2:
                    if line_is_start_publish(line):
                        result += '\n\n------\n\n'
                    # Página de duas colunas: Depois reseta para não ser lida
                    # mais nessa página.
                    two_col = 3
                if line['bbox'][1] <= rect_end[1]:
                    result += concatena_lines(line)
        elif (rect_start[0] <= 58.5 and rect_start[0] >= 53) and rect_end[
            1
        ] >= 827:
            if line['bbox'][0] >= 53 and line['bbox'][0] <= 54.4:
                if line['bbox'][1] >= rect_start[1]:
                    result += concatena_lines(line)
            elif line['bbox'][0] >= 319 and line['bbox'][0] <= 322.2:
                if not test:
                    test = True
                    if line_is_start_publish(line):
                        result += '\n\n------\n\n'
                if line['bbox'][1] <= rect_end[1]:
                    result += concatena_lines(line)
        elif (
            line['bbox'][1] >= rect_start[1] and line['bbox'][1] <= rect_end[1]
        ):
            if rect_start[0] >= 53 and rect_start[0] <= 58.5:
                if line['bbox'][0] >= 53 and line['bbox'][0] <= 54.4:
                    result += concatena_lines(line)
            else:
                if line['bbox'][0] >= 319 and line['bbox'][0] <= 320:
                    result += concatena_lines(line)

    return result


def get_all_(lines, rects_interested, first_page=False):
    result = ''
    end_ = (0.3449302017688751, 0.3479514718055725, 0.35645076632499695)

    if is_start_publish(lines):
        result += '\n\n------\n\n'
    if len(rects_interested) == 2 or (
        first_page and len(rects_interested) in [2, 3]
    ):
        start = rects_interested[0]['rect']
        end = rects_interested[-1]['rect']
        if len(rects_interested) == 3:
            start = rects_interested[1]['rect']

        if rects_interested[1]['width'] == 17.0:
            result += "**************** TITLE ****************"
        result += concat_page_complete(
            blocks=lines,
            rect_start=start,
            rect_end=end,
        )
    else:
        for i in range(0, len(rects_interested) - 1, 1):
            res = ''
            if rects_interested[i]['width'] == 17.0:
                res = "**************** TITLE ****************"
            res += concat_texts_blocks(
                lines=lines,
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
