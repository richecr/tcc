## Instalation

### multilingual_pdf2text:

#### No linux:

Deve ser instalado o [tesseract](https://tesseract-ocr.github.io/tessdoc/Installation.html):

portuguese: https://packages.ubuntu.com/focal/tesseract-ocr-por

```bash
sudo apt install tesseract-ocr
sudo apt install libtesseract-dev
sudo apt install tesseract-ocr-por
```

E então, basta instalar as dependencias e executar.

#### No windows:

##### Tesseract:

Deve ser instalado o [tesseract](https://github.com/UB-Mannheim/tesseract/wiki), baixar e instalar.

Após isso tem que instalar os dados para portugues: https://github.com/tesseract-ocr/tessdata

Basta baixar o por.traineddata e mover para a basta \tessdata, onde está instalado o tesseract-orc.

##### Poppler:

E também deve instalar o poppler: https://stackoverflow.com/questions/18381713/how-to-install-poppler-on-windows

Download Poppler Packaged for Windows: https://github.com/oschwartz10612/poppler-windows/releases

I threw together a quick repo with the latest Poppler prebuilt-binaries packaged with dependencies for Windows. Built with the help of conda-forge and poppler-feedstock. Includes the latest poppler-data.

No código adicionar: 

```python
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
```