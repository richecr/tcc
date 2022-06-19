import json


filename = 'output.jsonl'
name = 'PREGÃO PRESENCIAL SRP Nº 013/2021'

# Parei no 1170
with open(filename, 'r', encoding='utf-8') as json_file:
    for line in json_file.readlines():
        entity = json.loads(line)
        if name.upper() in entity['text'].upper():
            print(entity['id'])
