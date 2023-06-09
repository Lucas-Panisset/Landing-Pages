
#bibliotecas
from multiprocessing.connection import wait
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.alert import Alert 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui, pyperclip,unicodedata,sys

#variaveis e definições gerais
driver = webdriver.Chrome()
driver.get('https://app.greatpages.com.br/login')
wait = WebDriverWait(driver, 30)
driver.maximize_window()



month_dict = {'01': 'Janeiro', '02': 'Fevereiro', '03': 'Março', '04': 'Abril', '05': 'Maio', '06': 'Junho', 
                  '07': 'Julho', '08': 'Agosto', '09': 'Setembro', '10': 'Outubro', '11': 'Novembro', '12': 'Dezembro'}

cidades = ""
with open("C:/Users/Polozi/Desktop/lista.txt", "r") as f:
    cidades = [line.strip() for line in f]

links = ""
with open("C:/Users/Polozi/Desktop/links.txt", "r") as f:
    links = [line.strip() for line in f]

login = ''
with open("C:/Users/Polozi/Desktop/login.txt", "r") as f:
    login = [line.strip() for line in f]

global count
modelo = 1


#função que faz login no site
def Login(log, passwd):
    login = driver.find_element(By.ID, 'usuario')
    password = driver.find_element(By.ID, 'senha')

    login.send_keys(log)
    password.send_keys(passwd)
    pyautogui.press('Enter')
                    
#função para clicar nos locais necessários
def action_click(by, path):
    
    try:
        element = wait.until(EC.presence_of_element_located((by,path)))
        element.click()
    except:
        alert_present = False
        try:
            alert = alert.text
            alert_present = True
        except:
            pass
        if(alert_present):
            driver.switch_to.alert
            alert.accept()
        element = wait.until(EC.presence_of_element_located((by,path)))
        element.click()
        

def timed_action_click(by, path, timer):
    temp_wait = WebDriverWait(driver, timer)

    try:
        element = temp_wait.until(EC.presence_of_element_located((by,path)))
        element.click()
    except:
        alert_present = False
        try:
            alert = alert.text
            alert_present = True
        except:
            pass
        if(alert_present):
            driver.switch_to.alert
            alert.accept()
        element = temp_wait.until(EC.presence_of_element_located((by,path)))
        element.click()
        

#copia a pagina modelo variando automaticamente
def page_copy():
    global modelo
    match modelo:
        case 1:
            timed_action_click(By.XPATH, "//*[@id='184996']/td[4]/div/div", 1)
            modelo = 2
        case 2:
            timed_action_click(By.XPATH, "//*[@id='184997']/td[4]/div/div", 1)
            modelo = 3
        case 3:
            timed_action_click(By.XPATH, "//*[@id='184998']/td[4]/div/div", 1)
            modelo = 4
        case 4:
            timed_action_click(By.XPATH, "//*[@id='185000']/td[4]/div/div", 1)
            modelo = 1
   
    action_click(By.XPATH, "//*[@id='dropdown_1']/ul/li[3]")
   
    #abrir pagina
    
    action_click(By.XPATH, "//*[contains(text(), 'PALESTRA ABERTA - Cópia')]")
    
def page_renamer(cidade):
    global modelo
    try:
        city, date = cidade.split(",")
    except:
        city, date = cidade.split(";")
    day, month, year = date.split("/")
    
    action_click(By.XPATH, '//*[@id="admin_centro_area-acoes"]/div[3]/div')
    action_click(By.XPATH, '//*[@id="dropdown_1"]/ul/li[1]/span')
    
    nameinput = wait.until(
          EC.element_to_be_clickable((By.XPATH, '//*[@id="titulo"]')))
    nameinput.clear()
    
    numero = modelo - 1
    
    if(modelo == 1):
        numero = 4


    print(f"[{month_dict[month][0:3].upper()}/{year}] [M{numero}] [{city.upper()}] PALESTRA ABERTA - TESTE")

    nameinput.send_keys(f"[{month_dict[month][0:3].upper()}/{year}] [M{numero}] [{city.upper()}] PALESTRA ABERTA - TESTE")
    action_click(By.XPATH, '//*[@id="enviar_formulario_ajax"]')
    return city+','+day+','+month+","+year


#Organizador de string
def format_values(file_name):
    
    formated_values = []

    with open(file_name, 'r') as f:
        
        for line in f:
            line = line.strip()
            if not line: # Ignore empty lines
                continue
            try:
                line_parts = line.split(',')
            except:
                line_parts = line.split(';')
            if len(line_parts) != 2: # Ignore lines without city and date information
                continue

            city, date = line.strip().split(',')
            day, month, year = date.split('/')
            formated_date = f"Dia {day} de {month_dict[month]}"
            formated_city = f"Cidade {city.split('-')[0]}"
            formated_time = "Horário às 19h00"
            formated_entry = "Entrada 1kg de alimento não perecível"
            formated_address = "Endereço enviado por E-mail e WhatsApp"
            formated_values.append([formated_date, formated_city, formated_time, formated_entry, formated_address])
    
    return formated_values


def editar_pagina(formated_values):
   
    action_click(By.XPATH, '//*[@id="admin_botao_editar_pagina"]/span[2]')
    xpath_1 = "/html/body/div[3]/div[2]/div[2]/div/div[1]/div[1]/div[4]/div[2]/div/div[5]/div[1]/h2"
    xpath_2 = "/html/body/div[3]/div[2]/div[2]/div/div[1]/div[1]/div[4]/div[2]/div/div[4]/div[1]"
    xpath_3 = "/html/body/div[3]/div[2]/div[2]/div/div[1]/div[1]/div[4]/div[2]/div/div[4]/div[1]"
    xpath_4 = "/html/body/div[3]/div[2]/div[2]/div/div[1]/div/div[4]/div[2]/div/div[5]/div[1]"
   
    try:
        timed_action_click(By.XPATH, xpath_1, 1)
    except:
        try:
            timed_action_click(By.XPATH, xpath_2, 1)
        except:
            try:
                timed_action_click(By.XPATH, xpath_3, 1)
            except:
                timed_action_click(By.XPATH, xpath_4, 1)
   
    action_click(By.XPATH, '//*[@id="gpc-blocos_editor"]/div[9]/span[1]')
   
    pyperclip.copy(formated_values[0])
    pyautogui.hotkey('ctrl','a')
    pyautogui.hotkey('ctrl','v')
    pyautogui.press('Enter')
    pyperclip.copy(formated_values[1])
    pyautogui.hotkey('ctrl','v')
    pyautogui.press('Enter')
    pyperclip.copy(formated_values[2])
    pyautogui.hotkey('ctrl','v')
    pyautogui.press('Enter')
    pyperclip.copy(formated_values[3])
    pyautogui.hotkey('ctrl','v')
    pyautogui.press('Enter')
    pyperclip.copy(formated_values[4])

def editar_links(link):

    action_click(By.XPATH, '/html/body/div[3]/div[2]/div[2]/div/div[1]/div[1]/div[4]/div[2]/div')

    xpath_1 = "/html/body/div[3]/div[2]/div[2]/div/div[1]/div[1]/div[4]/div[2]/div/div[4]/form/fieldset"
    xpath_2 = "/html/body/div[3]/div[2]/div[2]/div/div[1]/div[1]/div[4]/div[2]/div/div[3]/form/fieldset"
    xpath_3 = "/html/body/div[3]/div[2]/div[2]/div/div[1]/div[1]/div[4]/div[2]/div/div[3]/form/fieldset"
    xpath_4 = "/html/body/div[3]/div[2]/div[2]/div/div[1]/div/div[4]/div[2]/div/div[4]/form/fieldset"

    try:
        timed_action_click(By.XPATH, xpath_1, 1)
    except:
        try:
            timed_action_click(By.XPATH, xpath_2, 1)
        except:
            try:
                timed_action_click(By.XPATH, xpath_3, 1)
            except:
                timed_action_click(By.XPATH, xpath_4, 1)
    
    action_click(By.XPATH, '//*[contains(text(), "Configurar")]')
    action_click(By.XPATH, "/html/body/div[3]/div[2]/div[3]/div[2]/div[2]/div[1]/div[5]/div[1]/div[2]/input")

    pyautogui.hotkey('ctrl','a')
    pyperclip.copy(link)
    pyautogui.hotkey('ctrl','v')

    if(modelo == 2):
        action_click(By.XPATH, '/html/body/div[3]/div[2]/div[2]/div/div[1]/div[1]/div[4]/div[2]/div')
        pyautogui.scroll(1000)
        action_click(By.XPATH, '/html/body/div[3]/div[2]/div[2]/div/div[1]/div[4]/div[4]/div[2]/div/div[2]/form/fieldset')
        action_click(By.XPATH, '//*[contains(text(), "Configurar")]')
        action_click(By.XPATH, "/html/body/div[3]/div[2]/div[3]/div[2]/div[2]/div[1]/div[5]/div[1]/div[2]/input")
        pyautogui.hotkey('ctrl','a')
        pyperclip.copy(link)
        pyautogui.hotkey('ctrl','v')

    action_click(By.XPATH, '/html/body/div[3]/div[2]/div[2]/div/div[1]/div[1]/div[4]/div[2]/div')
    action_click(By.XPATH, "/html/body/div[3]/div[1]/div/a")
    try:
        timed_action_click(By.XPATH, "/html/body/div[3]/div[2]/div[1]/div[1]/a",2)
    except:
        action_click(By.XPATH, "/html/body/div[3]/div[1]/div/a")
        sleep(.5)
        
        timed_action_click(By.XPATH, "/html/body/div[3]/div[2]/div[1]/div[1]/a", 15)






formated_values = format_values("C:/Users/Polozi/Desktop/lista.txt")
Login(login[0],login[1])
count = 0
for cidade in cidades:
    page_copy() 
    data = page_renamer(cidade)   
    editar_pagina(formated_values[count])
    editar_links(links[count])
    count += 1


