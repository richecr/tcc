# importa as bibliotecas necessárias
import PyPDF2

from utils import write_txt

# Abre o arquivo pdf
# lembre-se que para o windows você deve usar essa barra -> /
# lembre-se também que você precisa colocar o caminho absoluto
pdf_file = open('./pdfs_samples/page1.pdf', 'rb')

# Faz a leitura usando a biblioteca
read_pdf = PyPDF2.PdfFileReader(pdf_file)

# pega o numero de páginas
number_of_pages = read_pdf.getNumPages()

# lê a primeira página completa
page = read_pdf.getPage(0)

objs = page.getContents().getObject()
for obj in objs:
    print(obj)

# extrai apenas o texto
page_content = page.extractText()
print(page_content)
write_txt(page_content, filename='output_pypdf2.txt')

# remove as quebras de linha
# parsed = re.sub('n', '', parsed)
# print("Após eliminar as quebras")
# print(parsed)
