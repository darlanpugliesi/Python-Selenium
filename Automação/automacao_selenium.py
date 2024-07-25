from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Navegando até o Chrome
url = 'http://google.com'
browser = webdriver.Chrome()
browser.get(url)

# Realizando a busca na barra de pesquisa
search_bar = browser.find_element('xpath', '//*[@id="APjFqb"]')
search_bar.send_keys("Selenium Python Tutorial")
search_bar.send_keys(Keys.ENTER)

# Espera 1 segundo para garantir que carregue os resultados
time.sleep(1)

# Coletando os resultados da pesquisa
results = browser.find_elements('css selector', 'h3')

# Imprimindo os 5 primeiros resultados
for i, result in enumerate(results[:5]):
    print(f'Resultado {i+1}: {result.text}')

# Fechar o navegador
browser.quit()
