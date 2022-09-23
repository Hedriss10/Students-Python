import PyPDF2
import os

caminho_dos_pdfs = 'pdf'

novo_pdf = PyPDF2.PdfFileMerger()
for root, dirs, files in os.walk(caminho_dos_pdfs):
    for file in files:
        caminho_completo_arquivo = os.path.join(root, file)

        arquivo_pdf = open(caminho_completo_arquivo, 'rb')
        novo_pdf.append(arquivo_pdf)

    with open(f'{caminho_dos_pdfs}/novo_arquivo.pdf','wb') as arquivo3_pdf:
        novo_pdf.write(arquivo3_pdf)