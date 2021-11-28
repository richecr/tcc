import spacy

nlp = spacy.load("pt_core_news_sm")
f = open('./outputs/output_pdfminer3.txt', mode='r', encoding="utf-8")
doc = nlp(f.read())

for ent in doc.ents:
    print(ent.text + " - " + ent.label_)