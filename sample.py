# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from datetime import date,timedelta
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException,ElementClickInterceptedException,StaleElementReferenceException,TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import exceptions
from selenium.webdriver.support.select import Select
import math
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome import service as fs
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

import pandas as pd
import sys
import json
import re
import os
from collections import Counter
from csv import writer
import csv

import random
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime,date
import pandas as pd
from google.oauth2 import service_account
from googleapiclient.discovery import build
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import json
#ランダム数の作成
randomC = random.uniform(1,3)

##chormeのオプションを指定
options = webdriver.ChromeOptions()
options.add_argument("--headless")# ヘッドレスで起動するオプションを指定
options.page_load_strategy = 'eager'

options.add_argument("--incognito")
# options.add_argument("--no-startup-window")
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1200,1200")
options.add_argument("--no-sandbox")
options.add_argument("--enable-javascript")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument("--enable-webgl")
options.add_argument('--enable-accelerated-2d-canvas')
options.add_argument("--renderer-process-limit=5")

To_follow_filename = 'To_follow_TL.csv'


desiredcapabilities = DesiredCapabilities.CHROME.copy()
desiredcapabilities['platform'] = "MAC"
desiredcapabilities['version'] = "106.0.5249.61"
desiredcapabilities['javascriptEnabled'] = True
# print(desiredcapabilities)
path = os.getcwd()
# path = r'C:\Users\user\Desktop\python\HOMES'
CHROMEDRIVER = path + r'\chromedriver.exe'
new_driver = ChromeDriverManager().install()
chrome_service = fs.Service(executable_path=new_driver)

driver = webdriver.Chrome(desired_capabilities=options.to_capabilities(),options=options,service=chrome_service)
driver.implicitly_wait(30)


url = 'https://twitter.com/explore'
driver.get(url)
#ログインボタンをクリック
# browser.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div[2]/div[3]/a[2]').click()
# #IDを入力
# elem_mail = browser.find_element(By.CLASS_NAME,'r-30o5oe.r-1niwhzg.r-17gur6a.r-1yadl64.r-deolkf.r-homxoj.r-poiln3.r-7cikom.r-1ny4l3l.r-t60dpp.r-1dz5y72.r-fdjqy7.r-13qz1uu')
# elem_mail.send_keys('mememori8888@gmail.com')
# #PWを入力
# elem_pw = browser.find_element(By.NAME,'session[password]')
# elem_pw.send_keys('mm19830831')
# #ログインボタンをクリック
# elem_login = browser.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div')
# elem_login.click()

#allユーザーのdf
all_user_df = pd.DataFrame()
#追加用のdf
all_u_param_df = pd.DataFrame()
# スプレッドシートのcol_E_list

L_K_list = []
blank_list = ['']



#スプレッドシートの色塗りK,L列からユーザー名取得

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('ondemand-380101-8fe6bd6d0cb0.json', scope)
client = gspread.authorize(creds)

# スプレッドシートを開く
spreadsheet_name = '作業シート　運用版②'
worksheet_name = '色塗り'
sheet = client.open(spreadsheet_name).worksheet(worksheet_name)



# A列の値を取得
a_column = sheet.col_values(11)

# print(a_column)


IDinDashboard = list(filter(lambda x: x != '', a_column))

print(IDinDashboard)