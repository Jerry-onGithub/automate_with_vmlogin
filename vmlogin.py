# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 22:36:42 2022

@author: Jerry
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests
import time

mla_profile_id ='3072FF99-23AF-.....'    #change this with your profile id
mla_url ='http://127.0.0.1:35000/api/v1/profile/start?automation=true&profileId='+mla_profile_id
resp = requests.get(mla_url)
json = resp.json()
print(json['value'])
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", json['value'][7:])
driver = webdriver.Chrome(executable_path="C:/Users/.../Downloads/chromedriver_win32 (2)/chromedriver.exe", chrome_options=chrome_options)  #change this with your local path to your chromdriver(must be same version with your browser version)
driver.get('https://www.bing.com/')
executor_url = driver.command_executor._url
session_id = driver.session_id
print(executor_url)
print(session_id)
print('Ok, it is done')
time.sleep(5)
#driver.quit()
