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

Deve ser instalado o [tesseract](https://github.com/UB-Mannheim/tesseract/wiki), baixar e instalar.

E também deve instalar o poppler: https://stackoverflow.com/questions/18381713/how-to-install-poppler-on-windows

Other answers have linked to the correct download page for Windows users but do not specify how to install them for the uninitiated: https://blog.alivate.com.au/poppler-windows/

- Go to this page and download the binary of your choice. In this example we will download and use poppler-0.68.0_x86.

- Extract the archive file poppler-0.68.0_x86.7z into C:\Program Files. Thus, the directory structure should look something like this:

- Add ´C:\Program Files\poppler-0.68.0_x86\bin` to your system PATH by doing the following: Click on the Windows start button, search for Edit the system environment variables, click on Environment Variables..., under System variables, look for and double-click on PATH, click on New, then add C:\Users\Program Files\poppler-0.68.0_x86\bin, click OK.

- If you are using a terminal to execute poppler (e.g. running pdf2image in command line), you may need to reopen your terminal for poppler to work.

- Done.

No código adicionar: 

```python
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
```