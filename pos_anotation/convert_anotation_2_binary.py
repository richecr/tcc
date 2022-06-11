from html import entities
import json


filename = './pos_anotation/output_08_2021_anotacoes.json'
output = './pos_anotation/output_08_2021_classifier.json'

result = []
with open(filename, 'r', encoding='UTF-8') as json_file:
    data = json.load(json_file)
    for obj in data:
        entity = obj
        if len(entity['label']) == 0:
            entity['label'] = ['no']
        else:
            entity['label'] = ['yes']
        result.append(entity)

with open(output, 'w', encoding='UTF-8') as json_file:
    json.dump(result, json_file, indent=4)
