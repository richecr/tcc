import json


filename = 'all.json'
with open(filename, 'r', encoding='utf-8') as json_file:
    result = json.load(json_file)
    with open('output.jsonl', 'w') as outfile:
        for entry in result:
            entity = {'id': entry['id'], 'text': entry['data'], 'label': []}
            json.dump(entity, outfile)
            outfile.write('\n')
