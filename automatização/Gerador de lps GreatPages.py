# coding: UTF-8
#importando bibliotecas
from multiprocessing.connection import wait
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui, pyperclip

#definições
month_dict = {'01': 'Janeiro', '02': 'Fevereiro', '03': 'Março', '04': 'Abril', '05': 'Maio', '06': 'Junho', 
                  '07': 'Julho', '08': 'Agosto', '09': 'Setembro', '10': 'Outubro', '11': 'Novembro', '12': 'Dezembro'}

#iniciando o chrome
driver = webdriver.Chrome()
driver.get('https://app.greatpages.com.br/login')
count = 0
wait = WebDriverWait(driver, 60)

def click():
    



#Login 

def login():
    login = driver.find_element(By.ID, 'ususario')
    senha = driver.find_element(By.ID, 'senha')
    login.send_keys('poloziautomacao@gmail.com')
    senha.send_keys("jfDR2Dqg>'Vn/PW4")
    pyautogui.press("Enter")

