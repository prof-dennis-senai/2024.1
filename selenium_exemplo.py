import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from webdriver_manager.chrome import ChromeDriverManager

def browser(url):
    # Configuração do driver (Chrome, nesse caso)
    options = webdriver.ChromeOptions()

    # Executa o navegador sem interface gráfica
    #    options.add_argument('--headless')
    #    options.add_argument('--disable-gpu')

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    
    driver.get(url)

    time.sleep(1)
    driver.find_element('xpath', '/html/body/div[2]/div[4]/form/div[1]/div[1]/div[1]/div[1]/div[2]/textarea').send_keys('O que é selenium?')
    time.sleep(3)
    driver.find_element('xpath', '/html/body/div[2]/div[4]/form/div[1]/div[1]/div[3]/center/input[2]').click()

    time.sleep(5)

    driver.quit()


browser('https://google.com')