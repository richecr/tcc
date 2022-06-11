import json


filename = './pos_anotation/all.jsonl'
output = './pos_anotation/output_08_2021_anotacoes.json'

data = []
with open(filename, 'r', encoding='UTF-8') as json_file:
    for line in json_file.readlines():
        entity = json.loads(line)
        data.append(entity)

with open(output, 'w', encoding='UTF-8') as json_file:
    json.dump(data, json_file, indent=4)
