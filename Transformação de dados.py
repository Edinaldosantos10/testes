#bibliotecas
import pandas as pd
import tabula
import PyPDF2
import csv
import zipfile
import tabula

# Lê arquivo PDF 
df = tabula.read_pdf("/content/pdfs/PadrãoTISSComponenteOrganizacional202103.pdf", pages='79,80,81,82,83,84,85')
# converte PDF em CSV
df=tabula.convert_into("/content/pdfs/PadrãoTISSComponenteOrganizacional202103.pdf", "/content/pdfs/table.csv", output_format="csv", pages='79,80,81,82,83,84,85')

# é preciso instalar biblioteca de compressão:  pip install zipfile36

#Zipar csv num arquivo "Teste_Intuitive_Care_{seu_nome}.zip".
jungle_zip = zipfile.ZipFile('/content/pdfs/Teste_Intuitive_Care_edinaldosantos.zip', 'w')
jungle_zip.write('/content/pdfs/table.csv', compress_type=zipfile.ZIP_DEFLATED)
jungle_zip.close()
