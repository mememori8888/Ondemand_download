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
from google.oauth2 import service_account
from googleapiclient.discovery import build
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import json
import random
from webdriver_manager.chrome import ChromeDriverManager

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
creds = ServiceAccountCredentials.from_json_keyfile_name('ondemand2-381303-bce643df8a23.json', scope)
client = gspread.authorize(creds)

# スプレッドシートを開く
spreadsheet_name = '作業シート　運用版②'
worksheet_name = '色塗り'
sheet = client.open(spreadsheet_name).worksheet(worksheet_name)



# l,k列の値を取得
l_column = sheet.col_values(12)
k_column = sheet.col_values(11)
# print(a_column)


IDinDashboard = list(filter(lambda x: x != '', l_column))
IDinDashboard2 = list(filter(lambda x: x != '', k_column))

IDinDashboard.extend(IDinDashboard2)
count = len(IDinDashboard)
print(IDinDashboard)
for i in range(0,count,1):
    driver.get(url)
    # account_name = user_df.iloc[i,3]
    user_name = IDinDashboard[i]
    user_name = str(user_name)
    print('分岐点{}'.format(user_name))
    if user_name == '-':
        continue
    elif ',' in user_name:
        continue
    elif '/' in user_name or 'いいね' in user_name or '個' in user_name:
        continue
    else:
        pass
    print('{}番目の{}'.format(i,user_name))
    time.sleep(randomC)

    #サーチワードを入力
    
    try:
        elem_searchword = driver.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[1]/div[2]/div/div/div/form/div[1]/div/div/div/label/div[2]/div/input')

        elem_searchword.send_keys('@'+ user_name)
    except:
        output_list = [user_name,'接続エラー','接続エラー','接続エラー','接続エラー','接続エラー','接続エラー','接続エラー']
        print(output_list)
        
        #csvに出力
        with open('Stock_follow_user.csv',"a",newline='',encoding="cp932", errors='replace') as f:
            writer = csv.writer(f,quoting=csv.QUOTE_ALL)
            writer.writerow(output_list)
            f.close()
        #update用リスト
       
        L_K_list.append([output_list[0],output_list[2],output_list[3],output_list[4],output_list[5],output_list[6],output_list[7]])
        
        print(len(L_K_list))
        # all_u_param_df = pd.DataFrame([output_list])
        # all_user_df = pd.concat([all_user_df,all_u_param_df])
        continue
    time.sleep(randomC)
    #ポップアップの削除
    try:
        popup = driver.find_element(By.CLASS_NAME,'css-18t94o4.css-1dbjc4n.r-1niwhzg.r-1ets6dv.r-sdzlij.r-1phboty.r-rs99b7.r-1wzrnnt.r-19yznuf.r-64el8z.r-1ny4l3l.r-1dye5f7.r-o7ynqc.r-6416eg.r-lrvibr')
        popup.click()
        print('ポップアップ削除')
    except:
        pass
    #サーチワード入力後、サジェストをクリック
    # css-1dbjc4n r-1iusvr4 r-16y2uox
    try:
        sujest_elem = driver.find_element(By.CLASS_NAME,'css-1dbjc4n.r-12181gd.r-1pi2tsx.r-1ny4l3l.r-13qz1uu')
        sujest_elem.click()
    except:
        output_list = [user_name,'アカウントエラー','アカウントエラー','アカウントエラー','アカウントエラー','アカウントエラー','アカウントエラー','アカウントエラー']
        print(output_list)
        #追加用のdf
        with open('Stock_follow_user.csv',"a",newline='',encoding="cp932", errors='replace') as f:
            writer = csv.writer(f,quoting=csv.QUOTE_ALL)
            writer.writerow(output_list)
        f.close()
        #update用リスト
      
        L_K_list.append([output_list[0],output_list[2],output_list[3],output_list[4],output_list[5],output_list[6],output_list[7]])
      
        print(len(L_K_list))
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
        output_list = [user_name,'アカウントエラー','アカウントエラー','アカウントエラー','アカウントエラー','アカウントエラー','アカウントエラー','アカウントエラー']
        print(output_list)
        #追加用のdf
        with open('Stock_follow_user.csv',"a",newline='',encoding="cp932", errors='replace') as f:
            writer = csv.writer(f,quoting=csv.QUOTE_ALL)
            writer.writerow(output_list)
        f.close()
        #update用リスト
     
        L_K_list.append([output_list[0],output_list[2],output_list[3],output_list[4],output_list[5],output_list[6],output_list[7]])
     
        print(len(L_K_list))
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
    for height in range(0,12000,3000): 
        aftherheight = height + 3000
        # driver.execute_script("window.scrollTo(" + str(height) + ", " + str(aftherheight) + ");")
        time.sleep(randomC)
        # view	like	RT　最新ツイート
    try:
        messege_block = driver.find_elements(By.CLASS_NAME,'css-1dbjc4n.r-16y2uox.r-1wbh5a2.r-1ny4l3l')
    except:
        output_list = [user_name,'エラー','エラー','エラー','エラー','エラー','エラー','エラー']
        #追加用のdf
        with open('Stock_follow_user.csv',"a",newline='',encoding="cp932", errors='replace') as f:
            writer = csv.writer(f,quoting=csv.QUOTE_ALL)
            writer.writerow(output_list)
        f.close()
        #update用リスト
    
        L_K_list.append([output_list[0],output_list[2],output_list[3],output_list[4],output_list[5],output_list[6],output_list[7]])
       
        print(len(L_K_list))
        continue
    
    # ツイート内容
    
    messeges = driver.find_elements(By.CLASS_NAME,'css-901oao.r-18jsvk2.r-37j5jr.r-a023e6.r-16dba41.r-rjixqe.r-bcqeeo.r-bnwqim.r-qvutc0')
    messeges_name = driver.find_elements(By.CLASS_NAME,'css-1dbjc4n.r-1wbh5a2.r-dnmrzs')
    m_count = len(messeges)
    tweets = []
    tweets_name = []
    for param in messeges:
        param = param.text
        tweets.append(param)
    for param in messeges_name:
        param = param.text
        tweets_name.append(param)
        
    print('tweetの数は{}'.format(len(tweets)))
    if len(tweets) == 0:
        output_list = [user_name,'tweetなし','tweetなし','tweetなし','tweetなし','tweetなし','tweetなし','tweetなし']
        #追加用のdf
        with open('Stock_follow_user.csv',"a",newline='',encoding="cp932", errors='replace') as f:
            writer = csv.writer(f,quoting=csv.QUOTE_ALL)
            writer.writerow(output_list)
        f.close()
        #update用リスト
    
        L_K_list.append([output_list[0],output_list[2],output_list[3],output_list[4],output_list[5],output_list[6],output_list[7]])
       
        print(len(L_K_list))
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
    #比較用のリスト
    output_all_list = []
    rank_list = []
    for k in range(0,m_count,1):
        #messege_blockのなかにビューとライクに関するテキストを正規表現かリストで抜き出す
        RT_pattern = r'\d{1,8} 件のリツイート。'
        view_pattern = r'\d{1,8} 件の表示。' 
        like_pattern = r'\d{1,8} 件のいいね。'
        pined_pattern = r'固定されたツイート'
        RT_tweet_pattern = r'がリツイートしました'
        # #messege_blocks[]からカンマを消す
        # messege_blocks[k] = messege_blocks[k].replace(',','')
        # 正規表現パターンとテキストをマッチングする
        try:
            RT_match = re.search(RT_pattern, messege_blocks[k])
            view_match = re.search(view_pattern, messege_blocks[k])
            like_match = re.search(like_pattern, messege_blocks[k])
            pined_match = re.search(pined_pattern, messege_blocks[k])
            RT_tweet_match = re.search(RT_tweet_pattern, messege_blocks[k])
        except:
            continue
        try:
            tweet = tweets[k]
        except:
            tweet = '-'
            
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
            
        if RT_tweet_match:
           print("Match found", RT_tweet_match.group())
           if user_name == messeges_name[k]:
               pass
           else:
             continue
        else:
            print('対象アカウントのリツイートではない') 
        #万の書き換え
 
        if '万' in str(like_match) and '.' in str(like_match):
            like_match = str(like_match).replace('万','000').replace('.','')
        else:
            like_match = str(like_match).replace('万','0000')
            
        if '万' in str(RT_match) and '.' in str(RT_match):
            RT_match = str(RT_match).replace('万','000').replace('.','')
        else:
            RT_match = str(RT_match).replace('万','0000')
        
        if '万' in str(acount_follower) and '.' in str(acount_follower):
            acount_follower = str(acount_follower).replace('万','000').replace('.','')
        else:
            acount_follower = str(acount_follower).replace('万','0000')
            
        if '万' in str(view_match) and '.' in str(view_match):
            view_match = str(view_match).replace('万','000').replace('.','')
        else:
            view_match = str(view_match).replace('万','0000')
        
        
        try:
            if '万' in like_match or '万' in RT_match  or '万' in acount_follower  or '万' in view_match :
                rank = 'S'
                rank_list.append(rank)
            elif int(like_match) >= 500 and int(RT_match) >= 100 and int(acount_follower) >= 3000 and int(view_match) >= 1500:
                rank = 'S'
                rank_list.append(rank)
            elif '-' in like_match or '-' in RT_match  or '-' in acount_follower  or '-' in view_match :
                rank = '?'
                rank_list.append(rank)
            elif int(like_match) >= 300 and int(RT_match) >= 50 and int(acount_follower) >= 2000 and int(view_match) >= 1000:
                rank = 'A'
                rank_list.append(rank)
            elif int(like_match) >= 200 and int(RT_match) >= 30 and int(acount_follower) >= 1500 and int(view_match) >= 500:
                rank = 'B'
                rank_list.append(rank)
            elif int(like_match) >= 100 and int(RT_match) >= 10 and int(acount_follower) >= 1000 and int(view_match) >= 300:
                rank = 'C'
                rank_list.append(rank)
            else:
                rank = 'D'
                rank_list.append(rank)
        except:
            rank = '?'
            rank_list.append(rank)

        output_list = [user_name,acount_profile_blocks[2],combined_text,tweet,acount_follower,view_match,like_match,RT_match]
        output_list = [x.replace('\n', ' ') for x in output_list]
        
        output_all_list.append(output_list)
        #ランク分け
#         	like以下以上	RT以下以上	フォロアー	view
            # S	500	100	3000	1500
            # A	300	50	2000	1000
            # B	200	30	1500	500
            # C	100	10	1000	300
            
    print(output_all_list)
    
    count_all = len(output_all_list)
    comparison_list = []
    for q in range(0,count_all,1):
        try:
            like_filter = int(output_all_list[q][6])
        except:
            like_filter = 0
        #一番高いqを覚えておいて、qのtweetをBJ_BL_listに入れる
        comparison_list.append(like_filter)
        
    try:    
        max_value = max(comparison_list)
        max_index = comparison_list.index(max_value)
        print(max_value)
        print(max_index)
        print(comparison_list)
        # output_listを再定義する
        output_list = output_all_list[max_index]
        rank = rank_list[max_index]    
    except:
        output_list = [user_name,'エラー','エラー','エラー','エラー','エラー','エラー','エラー']
        rank = '?'  
        
    
    #update用リスト
    
    L_K_list.append([rank,output_list[0],output_list[2],output_list[3],output_list[4],output_list[5],output_list[6],output_list[7]])
   
    print(len(L_K_list))
    # print(output_list)
    #追加用のdf
    with open('Stock_follow_user.csv',"a",newline='',encoding="cp932", errors='replace') as f:
        writer = csv.writer(f,quoting=csv.QUOTE_ALL)
        writer.writerow(output_list)
    f.close()
    
# スプレッドシートを開く
import gspread
from oauth2client.service_account import ServiceAccountCredentials


scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('ondemand2-381303-bce643df8a23.json', scope)
client = gspread.authorize(creds)
spreadsheet_name = 'TWダッシュボード'
worksheet_name = 'TWダッシュボード'
sheet = client.open(spreadsheet_name).worksheet(worksheet_name)
# sheet.update('E19', col_E_list)
print(len(L_K_list))
sheet.update('CX19', L_K_list)
print('CX19 update')










