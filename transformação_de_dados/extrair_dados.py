# Bibliotecas
import tabula
import zipfile as zipf
import os
import wget
import pandas as pd

import csv
import numpy as np
import requests

# Listar PDF via web
lista_tabela = tabula.read_pdf("https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos/Anexo_I_Rol_2021RN_465.2021_RN599_RN600.pdf", pages="all")

# Download anexo1
link1 = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos/Anexo_I_Rol_2021RN_465.2021_RN599_RN600.pdf"
wget.download(link1, "anexooo1.pdf")

inp = (r"anexooo1.pdf")
oup = (r"anexo1.csv")

df = tabula.read_pdf(input_path=inp, pages="all")
tabula.convert_into(input_path=inp, output_path=oup, output_format="csv", pages="3-180", stream=True)

# Alterar nome das colunas OD e AMD  
colunas = pd.read_csv('./anexo1.csv', header=1)
colunas.head()


colunas.rename(columns={'OD': 'Seg. Odontológica'}, inplace=True)

colunas.rename(columns={'AMB': 'Seg. Ambulatorial'}, inplace=True)


colunas.to_csv('./anexo1.csv')      

# Criar Pasta para anexo csv ser compactado
pasta_nova = "Pasta_do_anexo1/"
if(not os.path.exists(pasta_nova)):
    os.mkdir(pasta_nova)

# Mover anexo1 para pasta nova
downloads_folder_path = r'C:\Teste Nivelamento' # para funcionar em minha máquina
arquivos = os.listdir(downloads_folder_path)

os.rename('anexo1.csv', 'Pasta_do_anexo1/anexoo1.csv')


# Compactar anexos
down_folder_path = r'C:\Teste Nivelamento\Pasta_do_anexo1'
anexos = os.listdir(down_folder_path)


def zipar(arqs):
    with zipf.ZipFile('Teste_Jonatas.zip','w', zipf.ZIP_DEFLATED) as z:
        for arq in arqs:
            if(os.path.isfile(arq)): 
                z.write(arq)
            else: 
                for root, dirs, files in os.walk(arq):
                    for f in files:
                        z.write(os.path.join(root, f))

zipar(['Pasta_do_anexo1','pasta_compactada'])

  
#for linha in leitor_csv:
     #print(linha)





    