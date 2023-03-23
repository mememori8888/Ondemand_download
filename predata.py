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
import openpyxl
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


###################################################################
# 以下を3つのwebサイトで行う


    # from TL import all_user_df
#ランダム数の作成
randomC = random.uniform(1,3)

path = os.getcwd()
##chormeのオプションを指定
options = webdriver.ChromeOptions()
# options.add_argument("--headless")# ヘッドレスで起動するオプションを指定
options.page_load_strategy = 'normal'

options.add_argument("--incognito")
# options.add_argument("--no-startup-window")
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1200,1200")
options.add_argument("--no-sandbox")
options.add_argument("--enable-javascript")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument('--disable-blink-features=AutomationControlled')
# options.add_argument("--enable-webgl")
# options.add_argument('--enable-accelerated-2d-canvas')
# options.add_argument("--renderer-process-limit=5")
options.add_experimental_option("prefs", {"download.default_directory": path })


CHROMEDRIVER = path + r'\chromedriver.exe'
new_driver = ChromeDriverManager().install()
chrome_service = fs.Service(executable_path=new_driver)

driver = webdriver.Chrome(options=options,service=chrome_service)
driver.implicitly_wait(randomC)


#twiftのurl
twift_url1 = 'http://133.130.107.106/admin/login.php'
twift_url2 = 'http://118.27.106.29/admin/login.php'
twift_url3 = 'http://133.130.103.212/admin/login.php'
# url_list = [twift_url1,twift_url3,twift_url2]
url_list = [twift_url2,twift_url1,twift_url3]
twift1_login = 'naoki0110@gmail.com'
twift2_login = 'momo123'
twift3_login = 'mori123'
# login_list = [twift1_login,twift3_login,twift2_login]
login_list = [twift2_login,twift1_login,twift3_login]

twift1_pw = '123123'
twift2_pw = '!%g-iYe)B_g5'
twift3_pw = '123123'
# pw_list = [twift1_pw,twift3_pw,twift2_pw]
pw_list = [twift2_pw,twift1_pw,twift3_pw]

twift1_file = 'twiftA'
twift2_file = 'twiftB'
twift3_file = 'twiftC'
file_list = [twift2_file,twift1_file,twift3_file]

# 日付取得　テキストの置き換えまで(2023-03-09をdatetime型にする。)
today = date.today()
today_str = today.strftime("%Y-%m-%d")
print('今日の日付は{}'.format(today_str))

# ファイル名の変更
# os.rename(dl1,twiftA)


#Unique_dfのファイル名
Twift_A_unique = 'twift_A_unique.xlsx'
Twift_B_unique = 'twift_B_unique.xlsx'
Twift_C_unique = 'twift_C_unique.xlsx'
Uniqe_files = [Twift_B_unique,Twift_A_unique,Twift_C_unique]

# os.rename(path1, path2)
# 
#  
#1day ago
one_days_ago = today - timedelta(days=1)
one_days_ago_str = one_days_ago.strftime("%Y-%m-%d")

#2day ago
two_days_ago = today - timedelta(days=2)
two_days_ago_str = two_days_ago.strftime("%Y-%m-%d")

# 3days ago

three_days_ago = today - timedelta(days=3)
three_days_ago_str = three_days_ago.strftime("%Y-%m-%d")

# 7days ago

seven_days_ago = today - timedelta(days=7)
seven_days_ago_str = seven_days_ago.strftime("%Y-%m-%d")

#14day ago
fourteen_days_ago = today - timedelta(days=14)
fourteen_days_ago_str = fourteen_days_ago.strftime("%Y-%m-%d")

# 30days ago
thirty_days_ago = today - timedelta(days=30)
thirty_days_ago_str = thirty_days_ago.strftime("%Y-%m-%d")

#45日前
days_ago_45 = today - timedelta(days=45)
days_ago_45_str = days_ago_45.strftime("%Y-%m-%d")
# 60days ago
sixty_days_ago = today - timedelta(days=60)
sixty_days_ago_str = sixty_days_ago.strftime("%Y-%m-%d")

#75days_ago
days_ago_75 = today - timedelta(days=75)
days_ago_75_str = days_ago_75.strftime("%Y-%m-%d")


# 90days ago
ninty_days_ago = today - timedelta(days=90)
ninty_days_ago_str = ninty_days_ago.strftime("%Y-%m-%d")


#180day ago
half_a_year_ago = today - timedelta(days=180)
half_a_year_ago_str = half_a_year_ago.strftime("%Y-%m-%d")

#360day ago
a_year_ago = today - timedelta(days=360)
a_year_ago_str = a_year_ago.strftime("%Y-%m-%d")

for web_count in range(0,len(url_list),1):
    print('{}番目のtwift'.format(web_count))
        # ダウンロードされるファイル 7 14 30 45 60 75 90
    dl1 = 'stat-data-{}.xlsx'.format(today_str)
    dl2 = 'stat-data-{} (1).xlsx'.format(today_str)
    dl3 = 'stat-data-{} (2).xlsx'.format(today_str)
    dl4 = 'stat-data-{} (3).xlsx'.format(today_str)
    dl5 = 'stat-data-{} (4).xlsx'.format(today_str)
    dl6 = 'stat-data-{} (5).xlsx'.format(today_str)
    dl7 = 'stat-data-{} (6).xlsx'.format(today_str)
    dl8 = 'account-data-{}.xlsx'.format(today_str)

    dl1 = dl1
    dl2 = dl2
    dl3 = dl3
    dl4 = dl4
    dl5 = dl5
    dl6 = dl6
    dl7 = dl7
    dl8 = dl8
    

    files = [dl1,dl2,dl3,dl4,dl5,dl6]
    driver.get(url_list[web_count])
    unique_file_name = Uniqe_files[web_count]
    try:
        #twiftにLogin
        login = driver.find_element(By.ID,'uname')
        login.send_keys(login_list[web_count])
        PW = driver.find_element(By.ID,'password')
        PW.send_keys(pw_list[web_count])
        login_button = driver.find_element(By.ID,'submit')
        login_button.click()
    except:
        continue
    #一括処理にアクセス
    batch_processing = driver.find_element(By.XPATH,'//*[@id="sidebar"]/ul/li[7]/a')
    batch_processing.click()
    #ファイルダウンロード
    all_account_data_dl = driver.find_element(By.XPATH,'//*[@id="accountdataget"]/span')
    driver.execute_script("window.scrollTo(" + str(0) + ", " + str(300) + ");")
    try:
        all_account_data_dl.click()
        print('アカウントファイルダウンロード完了')
    except:
        print('アカウントファイルダウンロード失敗')

    time.sleep(10)
    driver.execute_script("window.scrollTo(" + str(0) + ", " + str(600) + ");")

    #統計データの開始日付
    start_date = driver.find_element(By.ID,'datetimepicker1')
    end_date = driver.find_element(By.ID,'datetimepicker2')
    time.sleep(5)
    #14日前までの日付を入力
    start_date.send_keys(Keys.BACKSPACE)
    start_date.send_keys(Keys.BACKSPACE)
    start_date.send_keys(Keys.BACKSPACE)
    start_date.send_keys(Keys.BACKSPACE)
    start_date.send_keys(Keys.BACKSPACE)
    start_date.send_keys(Keys.BACKSPACE)
    start_date.send_keys(Keys.BACKSPACE)
    start_date.send_keys(Keys.BACKSPACE)
    start_date.send_keys(Keys.BACKSPACE)
    start_date.send_keys(Keys.BACKSPACE)
    time.sleep(10)
    start_date.send_keys(fourteen_days_ago_str)
    time.sleep(5)
    start_date.send_keys(Keys.ENTER)
    end_date.send_keys(Keys.BACKSPACE)
    end_date.send_keys(Keys.BACKSPACE)
    end_date.send_keys(Keys.BACKSPACE)
    end_date.send_keys(Keys.BACKSPACE)
    end_date.send_keys(Keys.BACKSPACE)
    end_date.send_keys(Keys.BACKSPACE)
    end_date.send_keys(Keys.BACKSPACE)
    end_date.send_keys(Keys.BACKSPACE)
    end_date.send_keys(Keys.BACKSPACE)
    end_date.send_keys(Keys.BACKSPACE)
    end_date.send_keys(Keys.BACKSPACE)
    time.sleep(5)
    end_date.send_keys(one_days_ago_str)
    time.sleep(5)
    end_date.send_keys(Keys.ENTER)
    # ファイルのダウンロード
    try:
        status_dl = driver.find_element(By.ID,'statusdataget')
        status_dl.click()
        print('14日前ダウンロード完了')
        # start_date = driver.find_element(By.ID,'datetimepicker1')
        # end_date = driver.find_element(By.ID,'datetimepicker2')
    except:
        print('14日前ダウンロード失敗')
        driver.refresh()
        start_date = driver.find_element(By.ID,'datetimepicker1')
        end_date = driver.find_element(By.ID,'datetimepicker2')
    time.sleep(30)
    #30日前から14日前までの日付を入力
    start_date.send_keys(Keys.BACKSPACE)
    start_date.send_keys(Keys.BACKSPACE)
    start_date.send_keys(Keys.BACKSPACE)
    start_date.send_keys(Keys.BACKSPACE)
    start_date.send_keys(Keys.BACKSPACE)
    start_date.send_keys(Keys.BACKSPACE)
    start_date.send_keys(Keys.BACKSPACE)
    start_date.send_keys(Keys.BACKSPACE)
    start_date.send_keys(Keys.BACKSPACE)
    start_date.send_keys(Keys.BACKSPACE)
    start_date.send_keys(Keys.BACKSPACE)
    time.sleep(5)
    start_date.send_keys(thirty_days_ago_str)
    end_date.send_keys(Keys.BACKSPACE)
    end_date.send_keys(Keys.BACKSPACE)
    end_date.send_keys(Keys.BACKSPACE)
    end_date.send_keys(Keys.BACKSPACE)
    end_date.send_keys(Keys.BACKSPACE)
    end_date.send_keys(Keys.BACKSPACE)
    end_date.send_keys(Keys.BACKSPACE)
    end_date.send_keys(Keys.BACKSPACE)
    end_date.send_keys(Keys.BACKSPACE)
    end_date.send_keys(Keys.BACKSPACE)
    end_date.send_keys(Keys.BACKSPACE)
    time.sleep(5)
    end_date.send_keys(fourteen_days_ago_str)
    time.sleep(5)
    end_date.send_keys(Keys.ENTER)
    # ファイルのダウンロード
    try:
        status_dl = driver.find_element(By.ID,'statusdataget')
        status_dl.click()
        print('30日前ダウンロード完了')
        driver.refresh()
        start_date = driver.find_element(By.ID,'datetimepicker1')
        end_date = driver.find_element(By.ID,'datetimepicker2')
    except:
        print('30日前ダウンロード失敗')
        driver.refresh()
        start_date = driver.find_element(By.ID,'datetimepicker1')
        end_date = driver.find_element(By.ID,'datetimepicker2')
        
    time.sleep(15)
    #45日前から30日前までの日付を入力　
    start_date.send_keys(Keys.BACKSPACE)
    start_date.send_keys(Keys.BACKSPACE)
    start_date.send_keys(Keys.BACKSPACE)
    start_date.send_keys(Keys.BACKSPACE)
    start_date.send_keys(Keys.BACKSPACE)
    start_date.send_keys(Keys.BACKSPACE)
    start_date.send_keys(Keys.BACKSPACE)
    start_date.send_keys(Keys.BACKSPACE)
    start_date.send_keys(Keys.BACKSPACE)
    start_date.send_keys(Keys.BACKSPACE)
    start_date.send_keys(Keys.BACKSPACE)
    time.sleep(5)
    start_date.send_keys(days_ago_45_str)
    end_date.send_keys(Keys.BACKSPACE)
    end_date.send_keys(Keys.BACKSPACE)
    end_date.send_keys(Keys.BACKSPACE)
    end_date.send_keys(Keys.BACKSPACE)
    end_date.send_keys(Keys.BACKSPACE)
    end_date.send_keys(Keys.BACKSPACE)
    end_date.send_keys(Keys.BACKSPACE)
    end_date.send_keys(Keys.BACKSPACE)
    end_date.send_keys(Keys.BACKSPACE)
    end_date.send_keys(Keys.BACKSPACE)
    end_date.send_keys(Keys.BACKSPACE)
    time.sleep(5)
    end_date.send_keys(thirty_days_ago_str)
    time.sleep(5)
    end_date.send_keys(Keys.ENTER)
    # ファイルのダウンロード
    try:
        status_dl = driver.find_element(By.ID,'statusdataget')
        status_dl.click()
        print('45日前ダウンロード完了')
        driver.refresh()
        start_date = driver.find_element(By.ID,'datetimepicker1')
        end_date = driver.find_element(By.ID,'datetimepicker2')
    except:
        print('45日前ダウンロード失敗')
        driver.refresh()
        start_date = driver.find_element(By.ID,'datetimepicker1')
        end_date = driver.find_element(By.ID,'datetimepicker2')


    time.sleep(15)

    #60日前から45日前までの日付を入力　
    start_date.send_keys(Keys.BACKSPACE)
    start_date.send_keys(Keys.BACKSPACE)
    start_date.send_keys(Keys.BACKSPACE)
    start_date.send_keys(Keys.BACKSPACE)
    start_date.send_keys(Keys.BACKSPACE)
    start_date.send_keys(Keys.BACKSPACE)
    start_date.send_keys(Keys.BACKSPACE)
    start_date.send_keys(Keys.BACKSPACE)
    start_date.send_keys(Keys.BACKSPACE)
    start_date.send_keys(Keys.BACKSPACE)
    start_date.send_keys(Keys.BACKSPACE)
    time.sleep(5)
    start_date.send_keys(sixty_days_ago_str)
    end_date.send_keys(Keys.BACKSPACE)
    end_date.send_keys(Keys.BACKSPACE)
    end_date.send_keys(Keys.BACKSPACE)
    end_date.send_keys(Keys.BACKSPACE)
    end_date.send_keys(Keys.BACKSPACE)
    end_date.send_keys(Keys.BACKSPACE)
    end_date.send_keys(Keys.BACKSPACE)
    end_date.send_keys(Keys.BACKSPACE)
    end_date.send_keys(Keys.BACKSPACE)
    end_date.send_keys(Keys.BACKSPACE)
    time.sleep(5)
    end_date.send_keys(days_ago_45_str)
    time.sleep(5)
    end_date.send_keys(Keys.ENTER)
    # ファイルのダウンロード
    try:
        status_dl = driver.find_element(By.ID,'statusdataget')
        status_dl.click()
        print('60日前ダウンロード完了')
        driver.refresh()
        start_date = driver.find_element(By.ID,'datetimepicker1')
        end_date = driver.find_element(By.ID,'datetimepicker2')
        
    except:
        print('60日前ダウンロード失敗')
        driver.refresh()
        start_date = driver.find_element(By.ID,'datetimepicker1')
        end_date = driver.find_element(By.ID,'datetimepicker2')

    
        
    time.sleep(15)

    #75日前から60日前までの日付を入力　
    start_date.send_keys(Keys.BACKSPACE)
    start_date.send_keys(Keys.BACKSPACE)
    start_date.send_keys(Keys.BACKSPACE)
    start_date.send_keys(Keys.BACKSPACE)
    start_date.send_keys(Keys.BACKSPACE)
    start_date.send_keys(Keys.BACKSPACE)
    start_date.send_keys(Keys.BACKSPACE)
    start_date.send_keys(Keys.BACKSPACE)
    start_date.send_keys(Keys.BACKSPACE)
    start_date.send_keys(Keys.BACKSPACE)
    start_date.send_keys(Keys.BACKSPACE)
    time.sleep(5)
    start_date.send_keys(days_ago_75_str)
    end_date.send_keys(Keys.BACKSPACE)
    end_date.send_keys(Keys.BACKSPACE)
    end_date.send_keys(Keys.BACKSPACE)
    end_date.send_keys(Keys.BACKSPACE)
    end_date.send_keys(Keys.BACKSPACE)
    end_date.send_keys(Keys.BACKSPACE)
    end_date.send_keys(Keys.BACKSPACE)
    end_date.send_keys(Keys.BACKSPACE)
    end_date.send_keys(Keys.BACKSPACE)
    end_date.send_keys(Keys.BACKSPACE)
    time.sleep(5)
    end_date.send_keys(sixty_days_ago_str)
    time.sleep(5)
    end_date.send_keys(Keys.ENTER)
    # ファイルのダウンロード
    try:
        status_dl = driver.find_element(By.ID,'statusdataget')
        status_dl.click()
        print('75日前ダウンロード完了')
        driver.refresh()
        start_date = driver.find_element(By.ID,'datetimepicker1')
        end_date = driver.find_element(By.ID,'datetimepicker2')
        
    except:
        print('75日前ダウンロード失敗')
        driver.refresh()
        start_date = driver.find_element(By.ID,'datetimepicker1')
        end_date = driver.find_element(By.ID,'datetimepicker2')
    
    #90日前から75日前までの日付を入力　
    start_date.send_keys(Keys.BACKSPACE)
    start_date.send_keys(Keys.BACKSPACE)
    start_date.send_keys(Keys.BACKSPACE)
    start_date.send_keys(Keys.BACKSPACE)
    start_date.send_keys(Keys.BACKSPACE)
    start_date.send_keys(Keys.BACKSPACE)
    start_date.send_keys(Keys.BACKSPACE)
    start_date.send_keys(Keys.BACKSPACE)
    start_date.send_keys(Keys.BACKSPACE)
    start_date.send_keys(Keys.BACKSPACE)
    start_date.send_keys(Keys.BACKSPACE)
    time.sleep(5)
    start_date.send_keys(ninty_days_ago_str)
    end_date.send_keys(Keys.BACKSPACE)
    end_date.send_keys(Keys.BACKSPACE)
    end_date.send_keys(Keys.BACKSPACE)
    end_date.send_keys(Keys.BACKSPACE)
    end_date.send_keys(Keys.BACKSPACE)
    end_date.send_keys(Keys.BACKSPACE)
    end_date.send_keys(Keys.BACKSPACE)
    end_date.send_keys(Keys.BACKSPACE)
    end_date.send_keys(Keys.BACKSPACE)
    end_date.send_keys(Keys.BACKSPACE)
    time.sleep(5)
    end_date.send_keys(days_ago_75_str)
    time.sleep(5)
    end_date.send_keys(Keys.ENTER)
    # ファイルのダウンロード
    try:
        status_dl = driver.find_element(By.ID,'statusdataget')
        status_dl.click()
        print('90日前ダウンロード完了')
        driver.refresh()
        start_date = driver.find_element(By.ID,'datetimepicker1')
        end_date = driver.find_element(By.ID,'datetimepicker2')
        
    except:
        print('90日前ダウンロード失敗')
        driver.refresh()
        start_date = driver.find_element(By.ID,'datetimepicker1')
        end_date = driver.find_element(By.ID,'datetimepicker2')
    
    #ファイルを7個ダウンロードしました。    
    list = []
    for file in files:    
        #ここは各ファイルをリストにまとめている。
        print(file)
        list.append(pd.read_excel(file,sheet_name = 0,header=0))
        
    df = pd.concat(list)
    #twift_*_unique.xlsxを読み込んで、pre_data_dfに入れる。その後concatする。
    pre_data_df = pd.read_excel(unique_file_name,engine='openpyxl')
    df = pd.concat([df,pre_data_df])
    #重複した行の削除
    uniqe_df = df.drop_duplicates()
    #エクセルに出力
    uniqe_df.to_excel(unique_file_name, engine='openpyxl', index=False)
    #ダウンロードしたファイルの削除
    for files in files:
        os.remove(files)

    os.remove(dl8)

    
    #ログアウト
    logout = driver.find_element(By.CLASS_NAME,'pull-right')
    logout.click()




