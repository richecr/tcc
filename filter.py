import json


filename = 'all.jsonl'
result = []
id = 6315
with open(filename, 'r', encoding='UTF-8') as json_file:
    for line in json_file.readlines():
        entity = json.loads(line)
        if len(entity['label']) > 0:
            entity['id'] = id
            result.append(entity)
            id += 1


with open('output.jsonl', 'w', encoding='utf-8') as outfile:
    for entry in result:
        json.dump(entry, outfile)
        outfile.write('\n')
