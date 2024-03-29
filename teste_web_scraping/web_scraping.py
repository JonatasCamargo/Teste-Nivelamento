# Importaçâo de Bibliotecas
from selenium import webdriver
from selenium.webdriver import chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pyautogui
from time import sleep
import wget
import os
import shutil
import zipfile as zipf

# Instanciar Opções (para corrigir de "abrir e fechar apagina rapido")
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

# Abrindo Página
driver = webdriver.Chrome(options=options,service=Service(ChromeDriverManager().install()))
driver.get('https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos')

# Maximizar Página
driver.maximize_window()
sleep(3)

# Sair de primeiro acesso
pyautogui.click(x=925, y=293)
sleep(1)

# Aceitar cokkies
driver.find_element(By.XPATH, """//html/body/div[5]/div/div/div/div/div[2]/button[3]""").click()


# Download anexo1
link1 = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos/Anexo_I_Rol_2021RN_465.2021_RN599_RN600.pdf"
wget.download(link1, "anexo1.pdf")

#Download anexo2
link2 = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos/Anexo_II_DUT_2021_RN_465.2021_RN599.pdf"
wget.download(link2, "anexo2.pdf")

# Criar Pasta para anexos
pasta_nova = "Pasta_de_anexos/"
if(not os.path.exists(pasta_nova)):
    os.mkdir(pasta_nova)

# Mover anexo1 e anexo2 para pasta nova
downloads_folder_path = r'C:\Teste Nivelamento' # para funcionar em minha máquina
arquivos = os.listdir(downloads_folder_path)

os.rename('anexo1.pdf', 'Pasta_de_anexos/anexoo1.pdf')
os.rename('anexo2.pdf', 'Pasta_de_anexos/anexoo2.pdf')

# Compactar anexos
down_folder_path = r'C:\Teste Nivelamento\Pasta_de_anexos'
anexos = os.listdir(down_folder_path)


def zipar(arqs):
    with zipf.ZipFile('anexos.zip','w', zipf.ZIP_DEFLATED) as z:
        for arq in arqs:
            if(os.path.isfile(arq)): 
                z.write(arq)
            else: 
                for root, dirs, files in os.walk(arq):
                    for f in files:
                        z.write(os.path.join(root, f))

zipar(['Pasta_de_anexos','pasta_compactada'])

# Fechar Navegador
driver.quit()
