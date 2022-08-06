# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 22:36:42 2022

@author: Jerry
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests
import time

mla_profile_id ='3072FF99-23AF-4B62-856E-FECB2510CE84'
mla_url ='http://127.0.0.1:35000/api/v1/profile/start?automation=true&profileId='+mla_profile_id
resp = requests.get(mla_url)
json = resp.json()
print(json['value'])
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", json['value'][7:])
driver = webdriver.Chrome(executable_path="C:/Users/Jerry/Downloads/chromedriver_win32 (2)/chromedriver.exe", chrome_options=chrome_options)
driver.get('https://www.bing.com/')
executor_url = driver.command_executor._url
session_id = driver.session_id
print(executor_url)
print(session_id)
print('ok it is done')
time.sleep(5)
#driver.quit()