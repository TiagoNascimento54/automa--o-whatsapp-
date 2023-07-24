import pandas as pd
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import urllib
import os

#servico =Service(GeckoDriverManager().install())
servico =Service(ChromeDriverManager().install())
contatos = pd.read_excel('Enviar.xlsx')

#ABRIR NAVEGADOR E ABRIR PAGINA DO WHATSAPP
navegador = webdriver.Chrome()
navegador.get('https://web.whatsapp.com/')
#FUNÇÃO PARA EXCREVER LER MENSAGEM DO BANCO DE DADOS
for i in contatos.index:
    nome=contatos.loc [i,'Nome']
    numero= contatos.loc [i, 'Número']
    mensagem= contatos.loc [i, 'Mensagem']
    arquivo = contatos.loc[i,'arquivo']
    texto = mensagem.replace('Fulano',nome)
    texto = urllib.parse.quote (texto)
    link = f'https://web.whatsapp.com/send?phone={numero}&text={texto}'
    navegador.get(link)
    while len(navegador.find_elements(By.ID,"side"))<1:
        time.sleep(5)
    time.sleep(7)
#FUNÇÃO PARA CLICAR NO BOTÃO DE ENVIAR  MENSAGEM  PAGINA DO WHATSUPP
    navegador.find_element (By.XPATH,'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]').click()
    time.sleep(6)
# CAMINHO PARA  PARA ENVIAR COM ANEXO 
    caminho_completo = os.path.abspath(f'arquivos/{arquivo}')
#FUNÇÃO PARA CLICAR NO CLIPES DA PAGINA DO WHATSUPP
    navegador.find_element(By.XPATH,'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/div').click()
    time.sleep(4)
#FUNÇÃO PARA CLICAR NO DOCUMENTO DA PAGINA DO WHATSUPP
    navegador.find_element(By.XPATH,'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/span/div/div/ul/li[5]/button/input').send_keys(caminho_completo)
    time.sleep(5)
##FUNÇÃO PARA CLICAR NO BOTÃO DE ENVIAR  DA PAGINA DO WHATSUPP
    navegador.find_element(By.XPATH,'//*[@id="app"]/div/div/div[3]/div[2]/span/div/span/div/div/div[2]/div/div[2]/div[2]/div').click()
    time.sleep(4)
time.sleep(10)


