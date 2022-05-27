import json


filename = 'all.json'
labeled = 1011

with open(filename, 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)
    for obj in data:
        if obj['id'] >= labeled:
            break

        if obj['label'] == []:
            print(obj['id'])
