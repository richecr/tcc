import json


filename = 'all.json'
labeled = 835

with open(filename) as json_file:
    data = json.load(json_file)
    for obj in data:
        if obj['id'] >= labeled:
            break

        if obj['label'] == []:
            print(obj['id'])
