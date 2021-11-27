import json


def write_txt(data, filename = "output.txt", dir = "./outputs/"):
    file = dir + filename
    with open(file, "w", encoding="utf-8") as f:
        f.write(data)


def write_json(data, filename = "output.txt", dir = "./outputs/"):
    file = dir + filename
    with open(file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)