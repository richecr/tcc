import json

name = 'PREGÃO ELETRÔNICO SRP Nº 040/2021'
filename = 'output.jsonl'

while True:
    name = input("> ")
    with open(filename, 'r', encoding='utf-8') as json_file:
        for line in json_file.readlines():
            entity = json.loads(line)
            if name.upper() in entity['text'].upper():
                print(entity['id'])
