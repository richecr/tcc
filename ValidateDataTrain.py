import json


filename = 'all.json'
labeled = 1151

def count_licitation(data):
    return len(list(filter(lambda x: x['label'] == ['yes'], data)))

def count_neg_licitation(data):
    return len(list(filter(lambda x: x['label'] == ['no'], data)))

with open(filename, 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)
    for obj in data:
        if obj['id'] >= labeled:
            break

        if obj['label'] == []:
            print(obj['id'])

    print("Qtd de Licitações: ", count_licitation(data))
    print("Qtd de Não Licitações: ", count_neg_licitation(data))