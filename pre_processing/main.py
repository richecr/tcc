import os
import re

directory = os.listdir('./outputs/pyxpdf_dou_ac')
caminhos = [
    os.path.join('./outputs/pyxpdf_dou_ac/', nome) for nome in directory
]
arquivos = [arq for arq in caminhos if os.path.isfile(arq)]
txts = [arq for arq in arquivos if arq.lower().endswith(".txt")]

for txt in txts:
    print(txt)
    with open(txt, "r") as file:
        text = file.read()
        s = re.search("^estado do acre", text.lower())
        print(s)
    break
