from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Entrando no site de notícias do G1
url = 'http://g1.globo.com'
browser = webdriver.Chrome()
browser.get(url)

# Tempo para carregar o site
time.sleep(1)

# Armazenando as noticias
noticias = browser.find_elements(By.CSS_SELECTOR, '[elementtiming="text-csr"]')

# Imprimindo as notícias
for i, noticia in enumerate(noticias):
    print(f'Notícia {i+1}: {noticia.text}')

# Fechar o navegador
browser.quit()