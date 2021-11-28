import spacy

nlp = spacy.load("pt_core_news_sm")
f = open('./outputs/output_pdfminer3.txt', mode='r', encoding="utf-8")
doc = nlp(f.read())

for i in doc.ents:
    print(str(i) + " - " + str(i.label_))