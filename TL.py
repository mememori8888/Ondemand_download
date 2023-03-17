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
import threading
#ランダム数の作成
randomC = random.uniform(1,3)

##chormeのオプションを指定
options = webdriver.ChromeOptions()
# options.add_argument("--headless")# ヘッドレスで起動するオプションを指定
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

filename = '/home/mamhidet/usr/Ondemand_co/twiftB_account.xlsx'
filename2 = '/home/mamhidet/usr/Ondemand_co/twiftA_account.xlsx'
filename3 = '/home/mamhidet/usr/Ondemand_co/twiftC_account.xlsx'
account_file_list = [filename,filename2,filename3]

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
col_E_list = []
BJ_BL_list = []
blank_list = ['','','','','','','','','']


#csvから8ユーザー名取得
for file_count in range(0,len(account_file_list),1):
    user_df = pd.read_excel(account_file_list[file_count])
    
    count = len(user_df)

    for i in range(0,count,1):
        driver.get(url)
        account_name = user_df.iloc[i,3]
        user_name = user_df.iloc[i,2]
        print('{}番目の{}'.format(i,user_name))
        print(account_file_list[file_count])
        time.sleep(randomC)

        #サーチワードを入力
        
        try:
            elem_searchword = driver.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[1]/div[2]/div/div/div/form/div[1]/div/div/div/label/div[2]/div/input')

            elem_searchword.send_keys('@'+ user_name)
        except:
            output_list = [account_name,user_name,'接続エラー','接続エラー','接続エラー','接続エラー','接続エラー','接続エラー','接続エラー']
            print(output_list)
            
            #csvに出力
            with open('all_user.csv',"a",newline='',encoding="cp932", errors='replace') as f:
                writer = csv.writer(f,quoting=csv.QUOTE_ALL)
                writer.writerow(output_list)
                f.close()
            #update用リスト
            col_E_list.append(output_list[3])
            col_E_list.append(blank_list)
            col_E_list.append(blank_list)
            col_E_list.append(blank_list)
            BJ_BL_list.append([output_list[6],output_list[7],output_list[8],output_list[0]])
            BJ_BL_list.append(blank_list)
            BJ_BL_list.append(blank_list)
            BJ_BL_list.append(blank_list)
            print(len(BJ_BL_list))
            # all_u_param_df = pd.DataFrame([output_list])
            # all_user_df = pd.concat([all_user_df,all_u_param_df])
            continue
        time.sleep(randomC)
        #サーチワード入力後、サジェストをクリック
        # css-1dbjc4n r-1iusvr4 r-16y2uox
        try:
            sujest_elem = driver.find_element(By.CLASS_NAME,'css-1dbjc4n.r-12181gd.r-1pi2tsx.r-1ny4l3l.r-13qz1uu')
            sujest_elem.click()
        except:
            output_list = [account_name,user_name,'アカウントエラー','アカウントエラー','アカウントエラー','アカウントエラー','アカウントエラー','アカウントエラー','アカウントエラー']
            print(output_list)
            #追加用のdf
            with open('all_user.csv',"a",newline='',encoding="cp932", errors='replace') as f:
                writer = csv.writer(f,quoting=csv.QUOTE_ALL)
                writer.writerow(output_list)
            f.close()
            #update用リスト
            col_E_list.append(output_list[3])
            col_E_list.append(blank_list)
            col_E_list.append(blank_list)
            col_E_list.append(blank_list)
            BJ_BL_list.append([output_list[6],output_list[7],output_list[8],output_list[0]])
            BJ_BL_list.append(blank_list)
            BJ_BL_list.append(blank_list)
            BJ_BL_list.append(blank_list)
            print(len(BJ_BL_list))
            continue
        # elem_searchword.send_keys(Keys.ENTER)
        time.sleep(randomC)
        try:
            #ユーザープロフィール取得
            # acount_name = driver.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[1]/div[1]/div/div/div/div/div/div[2]/div/h2/div/div/div/div/span[1]/span/span[1]').text
            acount_meta = driver.find_element(By.CLASS_NAME,'css-901oao.r-18jsvk2.r-37j5jr.r-a023e6.r-16dba41.r-rjixqe.r-bcqeeo.r-qvutc0').text
            # フォロアー	
            acount_profile_block = driver.find_element(By.CLASS_NAME,'css-1dbjc4n.r-1ifxtd0.r-ymttw5.r-ttdzmv').text
        except:
            output_list = [account_name,user_name,'アカウントエラー','アカウントエラー','アカウントエラー','アカウントエラー','アカウントエラー','アカウントエラー','アカウントエラー']
            print(output_list)
            #追加用のdf
            with open('all_user.csv',"a",newline='',encoding="cp932", errors='replace') as f:
                writer = csv.writer(f,quoting=csv.QUOTE_ALL)
                writer.writerow(output_list)
            f.close()
            #update用リスト
            col_E_list.append(output_list[3])
            col_E_list.append(blank_list)
            col_E_list.append(blank_list)
            col_E_list.append(blank_list)
            BJ_BL_list.append([output_list[6],output_list[7],output_list[8],output_list[0]])
            BJ_BL_list.append(blank_list)
            BJ_BL_list.append(blank_list)
            BJ_BL_list.append(blank_list)
            print(len(BJ_BL_list))
            continue
        acount_profile_blocks = acount_profile_block.splitlines()
        # acount_name = acount_profile_blocks[1]
        user_name =  acount_profile_blocks[2].replace('@','')
        
        acount_follower = [s for s in acount_profile_blocks if 'フォロワー' in s]
        acount_follower = acount_follower[0].replace('フォロワー','').replace(',','')
        acount_follower = acount_follower

        acount_followee = [s for s in acount_profile_blocks if 'フォロー中' in s]
        acount_followee = acount_followee[0].replace('フォロー中','').replace(',','')
        acount_followee = acount_followee
        
        #最新のツイートを抜き出すために、固定ツイートのテキストがあるか確認する。
        #アカウント名
        # print(acount_profile_blocks[1])
        # print(acount_profile_blocks[2])
        # print(acount_follower)
        # print(acount_meta)
        combined_text = f"{acount_profile_blocks[1]}\n{acount_profile_blocks[2]}\n{acount_meta}"
        # print(combined_text)
        time.sleep(randomC)
        #13000pixilずつスクロールするfor文
        for height in range(0,3000,3000): 
            aftherheight = height + 3000
            # driver.execute_script("window.scrollTo(" + str(height) + ", " + str(aftherheight) + ");")
            time.sleep(randomC)
            # view	like	RT　最新ツイート
        try:
            messege_block = driver.find_elements(By.CLASS_NAME,'css-1dbjc4n.r-16y2uox.r-1wbh5a2.r-1ny4l3l')
        except:
            output_list = [account_name,user_name,'エラー','エラー','エラー','エラー','エラー','エラー','エラー']
            #追加用のdf
            with open('all_user.csv',"a",newline='',encoding="cp932", errors='replace') as f:
                writer = csv.writer(f,quoting=csv.QUOTE_ALL)
                writer.writerow(output_list)
            f.close()
            #update用リスト
            col_E_list.append(output_list[3])
            col_E_list.append(blank_list)
            col_E_list.append(blank_list)
            col_E_list.append(blank_list)
            BJ_BL_list.append([output_list[6],output_list[7],output_list[8],output_list[0]])
            BJ_BL_list.append(blank_list)
            BJ_BL_list.append(blank_list)
            BJ_BL_list.append(blank_list)
            print(len(BJ_BL_list))
            continue
        
        # ツイート内容
        
        messeges = driver.find_elements(By.CLASS_NAME,'css-901oao.r-18jsvk2.r-37j5jr.r-a023e6.r-16dba41.r-rjixqe.r-bcqeeo.r-bnwqim.r-qvutc0')
        tweets = []
        for param in messeges:
            param = param.text
            tweets.append(param)
        print('tweetの数は{}'.format(len(tweets)))
        if len(tweets) == 0:
            output_list = [account_name,user_name,'エラー','エラー','エラー','エラー','エラー','エラー','エラー']
            #追加用のdf
            with open('all_user.csv',"a",newline='',encoding="cp932", errors='replace') as f:
                writer = csv.writer(f,quoting=csv.QUOTE_ALL)
                writer.writerow(output_list)
            f.close()
            #update用リスト
            col_E_list.append(output_list[3])
            col_E_list.append(blank_list)
            col_E_list.append(blank_list)
            col_E_list.append(blank_list)
            BJ_BL_list.append([output_list[6],output_list[7],output_list[8],output_list[0]])
            BJ_BL_list.append(blank_list)
            BJ_BL_list.append(blank_list)
            BJ_BL_list.append(blank_list)
            print(len(BJ_BL_list))
            continue
        else:
            pass
        # messeges_l = []
        # for param in messeges_l:
        #     param = param.text
        #     messeges_l.append(param)
        # print(messege_block)
        messege_blocks = []
        for param in messege_block:
            param = param.get_attribute("innerHTML")
            messege_blocks.append(param)

        m_count = len(messege_blocks)
        print('messege_blocksの数は{}'.format(m_count))
        
        for k in range(0,2,1):
            #messege_blockのなかにビューとライクに関するテキストを正規表現かリストで抜き出す
            RT_pattern = r'\d+ 件のリツイート。'
            view_pattern = r'\d{1,3}(,\d{3})* 件の表示。' 
            like_pattern = r'\d{1,3}(,\d{3})* 件のいいね。'
            pined_pattern = r'固定されたツイート'
            # #messege_blocks[]からカンマを消す
            # messege_blocks[k] = messege_blocks[k].replace(',','')
            # 正規表現パターンとテキストをマッチングする
            RT_match = re.search(RT_pattern, messege_blocks[k])
            view_match = re.search(view_pattern, messege_blocks[k])
            like_match = re.search(like_pattern, messege_blocks[k])
            pined_match = re.search(pined_pattern, messege_blocks[k])
            try:
                tweet = tweets[k]
            except:
                output_list = [account_name,user_name,'エラー','エラー','エラー','エラー','エラー','エラー','エラー']
                #追加用のdf
                with open('all_user.csv',"a",newline='',encoding="cp932", errors='replace') as f:
                    writer = csv.writer(f,quoting=csv.QUOTE_ALL)
                    writer.writerow(output_list)
                f.close()

                    #update用リスト
                col_E_list.append(output_list[3])
                col_E_list.append(blank_list)
                col_E_list.append(blank_list)
                col_E_list.append(blank_list)
                BJ_BL_list.append([output_list[6],output_list[7],output_list[8],output_list[0]])
                BJ_BL_list.append(blank_list)
                BJ_BL_list.append(blank_list)
                BJ_BL_list.append(blank_list)
                print(len(BJ_BL_list))
                continue
                
            # 出力用リスト
            output_list = []
            # マッチが見つかった場合は、マッチング結果を出力する
            
            if RT_match:
                print('{}の{}番目のツイート'.format(acount_profile_blocks[1],k))
                print("Match found:", RT_match.group())
                RT_match = RT_match.group().replace(' 件のリツイート。','')
            else:
                RT_match = '-'

            if view_match:
                print("Match found:", view_match.group())
                view_match = view_match.group().replace(' 件の表示。','')
            else:
                view_match = '-'

            if like_match:
                print("Match found:", like_match.group())
                like_match = like_match.group().replace(' 件のいいね。','')
            else:
                like_match = '-'

            if pined_match:
                print("Match found:", pined_match.group())
                continue    
            else:
                print("固定ツイートではない")

            output_list = [account_name,user_name,acount_profile_blocks[2],combined_text,tweet,acount_follower,view_match,like_match,RT_match]
            output_list = [x.replace('\n', ' ') for x in output_list]
            #update用リスト
            col_E_list.append(output_list[3])
            col_E_list.append(blank_list)
            col_E_list.append(blank_list)
            col_E_list.append(blank_list)
            BJ_BL_list.append([output_list[6],output_list[7],output_list[8],output_list[0]])
            BJ_BL_list.append(blank_list)
            BJ_BL_list.append(blank_list)
            BJ_BL_list.append(blank_list)
            print(len(BJ_BL_list))
            # print(output_list)
            #追加用のdf
            with open('all_user.csv',"a",newline='',encoding="cp932", errors='replace') as f:
                writer = csv.writer(f,quoting=csv.QUOTE_ALL)
                writer.writerow(output_list)
            f.close()
            break
# スプレッドシートを開く
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import xlrd

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('ondemand-380101-8fe6bd6d0cb0.json', scope)
client = gspread.authorize(creds)
spreadsheet_name = 'TWダッシュボード のコピー'
worksheet_name = 'TWダッシュボード'
sheet = client.open(spreadsheet_name).worksheet(worksheet_name)
sheet.update('E19', col_E_list)
print(len(BJ_BL_list))
sheet.update('BT19', BJ_BL_list)










    #     #2表示されているツイートのいいねを可能な限り取得、その数を出力。
    #     elem_iine = driver.find_elements(By.CSS_SELECTOR,'div > div > article > div > div > div > div.css-1dbjc4n.r-18u37iz > div.css-1dbjc4n.r-1iusvr4.r-16y2uox.r-1777fci.r-kzbkwu > div:nth-child(2) > div.css-1dbjc4n.r-18u37iz.r-1wtj0ep.r-1s2bzr4.r-1mdbhws > div:nth-child(3) > div')
    #     number = len(elem_iine)
    #     print(user_name)
    #     print(number)
    #     #3取得できたいいねの"data-testid属性"のテキストを取得、その後、#2の数でループを回しいいねをクリック
    #     for i in range(0,number,1):
    #         like = elem_iine[i].get_attribute("data-testid")
    #         print(like)
    #         if like == 'like':
    #             driver.execute_script("arguments[0].click();", elem_iine[i])
    #             #elem_iine[i].send_keys(Keys.PAGE_DOWN)
    #             time.sleep(randomC)
    #         else:
    #             #4すでにいいねがされているものは、「すでにいいね」と出力
    #             print('すでにいいね')
                
    #     #この後スクロールダウンしてから、繰り返す。

    # #バックボタンで戻る
    # back_elem = driver.find_element(By.CLASS_NAME,'css-18t94o4.css-1dbjc4n.r-1niwhzg.r-42olwf.r-sdzlij.r-1phboty.r-rs99b7.r-2yi16.r-1qi8awa.r-1ny4l3l.r-o7ynqc.r-6416eg.r-lrvibr')
    # back_elem.click()
