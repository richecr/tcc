import os
import json


dir = './tcc/outputs/json/2021/11/'
directory = os.listdir(dir)
caminhos = [os.path.join(dir, name) for name in directory]
arquivos = [arq for arq in caminhos if os.path.isfile(arq)]
jsons = [arq for arq in arquivos if arq.lower().endswith('.json')]

count = 1
result = []
for path in jsons:
    with open(path) as f:
        data = json.load(f)
        for entity in data.keys():
            if isinstance(data[entity], list):
                for act in data[entity]:
                    result.append({'id': count, 'text': act, 'label': []})
                    count += 1
            else:
                titles = data[entity].keys()
                for title in titles:
                    for act in data[entity][title]:
                        result.append({'id': count, 'text': act, 'label': []})
                        count += 1

json_object = json.dumps(result, indent=4)

with open('output.jsonl', 'w') as outfile:
    for entry in result:
        json.dump(entry, outfile)
        outfile.write('\n')
