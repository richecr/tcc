import json


def write_txt(data, filename='output.txt', dir='./tcc/outputs/', mode='w'):
    file = dir + filename
    with open(file, mode=mode, encoding='utf-8') as f:
        f.write(data)


def write_txt_pb(
    data, filename='output.txt', dir='./outputs/dou_pb/', mode='w'
):
    file = dir + filename
    with open(file, mode=mode, encoding='utf-8') as f:
        f.write(data)


def write_json(data, filename='output.json', dir='./tcc/outputs/json/'):
    file = dir + filename
    with open(file, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)
