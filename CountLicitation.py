import json


filename = 'all.json'
labeled = 651

with open(filename, 'r', encoding='utf-8') as json_file:
    count = 0
    data = json.load(json_file)
    for obj in data:
        if obj['id'] >= labeled:
            break

        if obj['label'] == ['yes']:
            count += 1
            print(obj['id'])

    print(count)
