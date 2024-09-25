import pandas as pd
import urllib3
from bs4 import BeautifulSoup

def faz_requisicao(site):
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    manager = urllib3.PoolManager()
    return manager.request('GET', site, headers={'User-Agent': 'Mozilla/5.0'})

def le_site(site):
    response = faz_requisicao(site)
    return BeautifulSoup(response.data, 'html.parser')

# URL do site
url = 'https://www.horariodebrasilia.org/'

# Faz a leitura do site
bs = le_site(url)

# Encontra a tag com o ID 'relogio'
tag_hora = bs.find('p', id='relogio')

# Verifica se a tag foi encontrada e imprime o texto
if tag_hora:
    print("Hora atual:", tag_hora.text)
else:
    print("Tag com ID 'relogio' não encontrada.")