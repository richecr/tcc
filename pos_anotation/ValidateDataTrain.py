import json


filename = './pos_anotation/output_08_2021_anotacoes.json'


def label_contains_type(labels, type):
    return len(list(filter(lambda x: x[-1] == type, labels))) > 0


count_neg_licitation = 0
count_pos_licitation = 0
with open(filename, 'r', encoding='UTF-8') as json_file:
    data = json.load(json_file)
    for obj in data:
        if len(obj['label']) == 0:
            count_neg_licitation += 1
        else:
            count_pos_licitation += 1

    print('Qtd de Licitações: ', count_pos_licitation)
    print('Qtd de Não Licitações: ', count_neg_licitation)
