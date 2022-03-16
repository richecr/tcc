import spacy

nlp = spacy.load('pt_core_news_sm')
# f = open('./outputs/output_pdfminer3.txt', mode='r', encoding='utf-8')
doc = nlp("PORTARIA Nº 2.432, DE 15 DE DEZEMBRO DE 2021. A Secretária de Estado de Educação, Cultura e Esportes, no uso das atribuições que lhe confere o Decreto nº 8.821, de 03 de maio de 2021, publicado no Diário Oficial do Estado nº 13.035, de 04 de maio de 2021, e tendo  em vista as razões apresentadas mediante o MEM Nº 02/CPAD/SEE/2021, RESOLVE: Art.1º Determinar nos termos do art. 183, § 7º, da Lei Complementar Estadual nº 39/1993, conforme redação em vigor mediante LC nº 319, de 13  de junho de 2016, a prorrogação por mais 15 (quinze) dias do prazo para  conclusão dos trabalhos inerentes ao Processo Administrativo Disciplinar  nº 0014.005654.00286/2021-91, submetido ao Rito Sumário, instaurado a  partir da Portaria nº 1.957, de 29 de setembro de 2021, publicada no Diário  Oficial do Estado “on-line” nº 13.146, de 14 de outubro de 2021. Art. 2º Esta Portaria entra em vigor na data de sua publicação, com  efeito a contar de 13 de dezembro de 2021. Registre-se. Publique-se. Cumpra-se. MARIA DO SOCORRO NERI MEDEIROS DE SOUZA Secretária de Estado de Educação, Cultura e Esportes GOVERNO DO ESTADO DO ACRE SECRETARIA DE ESTADO DE EDUCAÇÃO, CULTURA E ESPORTES  GABINETE DA SECRETÁRIA")

for ent in doc.ents:
    print(ent.text + ' - ' + ent.label_)
