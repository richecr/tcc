import json


filename = 'all.json'

# Parei no 1170
with open(filename, 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)
    for obj in data:
        if "AVISO DE LICITAÇÃO" in obj['data']:
            print(obj['id'])

