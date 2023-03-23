from datetime import datetime,date
import pandas as pd
from google.oauth2 import service_account
from googleapiclient.discovery import build
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import json

#To_follow_TL.py用のファイル名
To_follow_TL_file_list = ['To_follow_B.xlsx','To_follow_A,xlsx','To_follow_C.xlsx']

#認証キー
outh_key = 'ondemand2-381303-bce643df8a23.json'

#その次の右側

#twift*_account.xlsx
twift_account_list = ['twiftB_account.xlsx','twiftA_account.xlsx','twiftC_account.xlsx']
# 今日の日付
today = date.today()
today_str = today.strftime("%Y-%m-%d")

today_datetime = datetime.combine(today, datetime.min.time())
# # 認証情報の作成
# SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']
# SERVICE_ACCOUNT_FILE = 'ondemand-380101-8fe6bd6d0cb0.json'
# creds = None
# creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# # Google Sheets APIの設定
# SPREADSHEET_ID = '1_b2RuWj3j1raSZqAcku1EYD_U4zniwPGwPIuYuzsG24'
# SHEET_NAME = 'コンテナA（旧）'
# service = build('sheets', 'v4', credentials=creds)
# sheet = service.spreadsheets()



import gspread
from oauth2client.service_account import ServiceAccountCredentials

# 認証情報を取得する
scope = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('ondemand2-381303-bce643df8a23.json', scope)

# 認証情報を使用してgspreadをインスタンス化する
client = gspread.authorize(creds)

# スプレッドシートIDを指定する
spreadsheet_id = '18s-x127g9XumN-ggQQD0JU7jmKlYJPdNG9HhNBktQjc'

# シート名を指定する
worksheet_name = 'コンテナA（旧）'
worksheet_name2 = 'コンテナB（新）'

# スプレッドシートを開く
worksheet = client.open_by_key(spreadsheet_id).worksheet(worksheet_name)

# 全ての値を取得する
values = worksheet.get_all_values()
array_sliced = [i[1:] for i in values]

# スプレッドシートを開く
worksheet2 = client.open_by_key(spreadsheet_id).worksheet(worksheet_name2)

# 全ての値を取得する
values = worksheet2.get_all_values()
array_sliced2 = [i[1:] for i in values]


# データフレームに変換
df = pd.DataFrame(array_sliced)
df2 = pd.DataFrame(array_sliced2)


#コンテナA (旧)
GS_master_df = pd.DataFrame(columns=['account_name','user_name','followed','s_follow','s_follow2'])
GS_master_df['account_name'] = df.iloc[:,0]
GS_master_df['user_name'] = df.iloc[:,1]
GS_master_df['followed'] = df.iloc[:,25]
GS_master_df['s_follow'] = df.iloc[:,19]
GS_master_df['s_follow2'] = df.iloc[:,20]
print(GS_master_df)

#コンテナB (新)
GS_master_df2 = pd.DataFrame(columns=['account_name','user_name','followed','s_follow','s_follow2'])
GS_master_df2['account_name'] = df2.iloc[:,0]
GS_master_df2['user_name'] = df2.iloc[:,1]
GS_master_df2['followed'] = df2.iloc[:,26]
GS_master_df2['s_follow'] = df2.iloc[:,17]
GS_master_df2['s_follow2'] = df2.iloc[:,18]
print(GS_master_df2)
GS_master_df = pd.concat([GS_master_df,GS_master_df2])

GS_master_df.to_csv('GS_master.csv')
# print(GS_master_df['followed'])
#GS_master_dfの使い方としては、all_user_dfのユーザIDと照合して、フォロー先アカウントをリストに入れる。
 # update用のリスト　2次元配列

# print(GS_master_df['followed'])
#GS_master_dfの使い方としては、all_user_dfのユーザIDと照合して、フォロー先アカウントをリストに入れる。
 # update用のリスト　2次元配列
account_all_list = []
TL_list_new = []
account_TL_list = []
account_Sall_list = []

'''
ダブり
Meretseger_G
'''
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('ondemand2-381303-bce643df8a23.json', scope)
client = gspread.authorize(creds)

# スプレッドシートを開く
spreadsheet_name = 'TWダッシュボード'
worksheet_name = 'TWダッシュボード'
sheet = client.open(spreadsheet_name).worksheet(worksheet_name)



# E列の値を取得
a_column = sheet.col_values(5)

# print(a_column)


IDinDashboard = list(filter(lambda x: x != '', a_column))
# IDinDashboard = list(filter(lambda x: x != 'moonstrawberrys', a_column))

# twift*_account.xlsxをall_user_dfに読み込む for分開始
all_user_df = pd.DataFrame([IDinDashboard])
# print(all_user_df)
# count = len(all_user_df)
count = len(IDinDashboard)
print(count)


    



filtered_df = pd.DataFrame(columns=['account_name','user_name','followed','s_follow','s_follow2'])
#エラー時のデータフレーム
error_list = ['エラー','エラー','エラー','エラー','エラー']
error_df = pd.DataFrame([error_list],columns=['account_name','user_name','followed','s_follow','s_follow2'])

for i in range(0,count,1):
    if IDinDashboard[i] == 'moonstrawberrys' or  IDinDashboard[i] == '月乃' or IDinDashboard[i] == 'user名':
        continue
    else:
        GS_sort_AUD = GS_master_df.loc[GS_master_df['user_name'] == IDinDashboard[i],:]
        if GS_sort_AUD.empty:
            filtered_df = pd.concat([filtered_df,error_df])
        else:
            filtered_df = pd.concat([filtered_df,GS_sort_AUD])

# filtered_dfを使って、s_follow,s_follow2を抽出する

filtered_df.to_csv('filtered.csv')
# リストをさくせいし、期間別にセルを決める。最新、30日前、60日前、90日前、180日前、360日前
col = [
    '最新',
    '30日前',
    '60日前',
    '90日前',
    '180日前',
    '360日前',
    'エラー',
    
    
    ]

# test_list = filtered_df.values.tolist()
# print(test_list)


TL_list_7ago = []
TL_list_14ago = []
TL_list_21ago = []
TL_list_28ago = []
TL_list_35ago = []
TL_list_error = []

# GS_master_dfの使いどころは、
f_count = len(filtered_df)

account_all_df = pd.DataFrame(columns = col)

for k in range(0,f_count,1):
    
    print('f_countの数は{}'.format(k))
    test_list = filtered_df.iloc[k,2].split(',')
    #
    try:
        s_follow = filtered_df.iloc[k,3]
        
    except:
        s_follow = '-'
    try:
        s_follow2 = filtered_df.iloc[k,4]
        
    except:
        s_follow2 = '-'
    #もしdelta.daysが0-7なら最新,7-15なら1，2週間前、16-30 なら3-4週間前 31-60なら2ヶ月前、61-90なら3ヶ月前  91-360はそれ以前     
    account_X_list = []
    key_value_list_pre1 = []
    key_value_list_pre2 = []
    key_value_list_pre3 = []
    key_value_list_pre4 = []
    key_value_list_pre5 = []
    key_value_list_pre6 = []
    error_list = []

            
    try:
        # 辞書を作成する
        my_dict = {test_list[i]: test_list[i+1] for i in range(0, len(test_list), 2)}
        for key,value in my_dict.items():
            try:
                key_obj = datetime.strptime(key, "%Y/%m/%d")
                # formatted_key = key_obj.strftime("%Y-%m-%d")
                delta = today_datetime - key_obj
                delta_days = delta.days
                # print(type(delta.days))
                # print('本日との差は{}日'.format(delta.days))
                # print('本日との差は{}日'.format(delta.months))
                
                if 1 <= delta_days <= 7:
                    key_value_list_pre1.append(value)
                elif 30 <= delta_days <= 59:
                    key_value_list_pre2.append(value)
                elif 60 <= delta_days <= 89:
                    key_value_list_pre3.append(value)
                elif 90 <= delta_days <= 119:
                    key_value_list_pre4.append(value)
                elif 180 <= delta_days <= 209:
                    key_value_list_pre5.append(value)
                elif 360 <= delta_days <= 389:
                    key_value_list_pre6.append(value)
            except:
                error_list.append(value)
                # print('計算できなかった日付は{} {}'.format(key,value))    
    except:
        pass
    #listのなかを一つのアカウントにする
    if len(key_value_list_pre1) == 0:
        pass
    else:
        key_valeu_list_pre1 = key_value_list_pre1[0]

    if len(key_value_list_pre2) == 0:
        pass
    else:
        key_valeu_list_pre2 = key_value_list_pre2[0]

    if len(key_value_list_pre3) == 0:
        pass
    else:
        key_valeu_list_pre3 = key_value_list_pre3[0]

    if len(key_value_list_pre4) == 0:
        pass
    else:
        key_valeu_list_pre4 = key_value_list_pre4[0]

    if len(key_value_list_pre5) == 0:
        pass
    else:
        key_valeu_list_pre5 = key_value_list_pre5[0]

    if len(key_value_list_pre6) == 0:
        pass
    else:
        key_valeu_list_pre6 = key_value_list_pre6[0]
    
    # TL.py用にリストを作成する優先順位は最新、7日前、14日前
    TL_list_new.append(key_value_list_pre1)
    TL_list_7ago.append(key_value_list_pre2)
    TL_list_14ago.append(key_value_list_pre3)
    TL_list_21ago.append(key_value_list_pre4)
    TL_list_28ago.append(key_value_list_pre5)
    TL_list_35ago.append(key_value_list_pre6)
    TL_list_error.append(error_list)
    #優先順位順に並べ替える
    TL_list_new.extend(TL_list_7ago)
    TL_list_new.extend(TL_list_14ago)  
    TL_list_new.extend(TL_list_21ago)  
    TL_list_new.extend(TL_list_28ago)  
    TL_list_new.extend(TL_list_35ago)  
    TL_list_new.extend(error_list)  
    

    # リストをテキスト化する
    # my_list_as_text = json.dumps(my_list)
    key_value_list_pre1_text = json.dumps(key_value_list_pre1)
    key_value_list_pre2_text = json.dumps(key_value_list_pre2)
    key_value_list_pre3_text = json.dumps(key_value_list_pre3)
    key_value_list_pre4_text = json.dumps(key_value_list_pre4)
    key_value_list_pre5_text = json.dumps(key_value_list_pre5)
    key_value_list_pre6_text = json.dumps(key_value_list_pre6)
    error_list_text = json.dumps(error_list)
    #account_x_listとblanklist sフォローはここに入れる
    account_X_list = [
                        key_value_list_pre1_text,
                        key_value_list_pre2_text,
                        key_value_list_pre3_text,
                        key_value_list_pre4_text,
                        key_value_list_pre5_text,
                        key_value_list_pre6_text,
                        error_list_text,
                       
                        ]
    
    
    
    account_X_list = [s.replace("[", "") for s in account_X_list]
    account_X_list = [s.replace("]", "") for s in account_X_list]
    account_X_list = [s.replace('"', "") for s in account_X_list]
    blank_list = ['','','','','','','','','',]
    #account_all_listに入れていく
    account_all_list.append(account_X_list)
 
    
    #twitter用のリスト
    account_Sfollow_list = [s_follow]
    account_Sfollow_list = [s.replace("[", "") for s in account_Sfollow_list]
    account_Sfollow_list = [s.replace("]", "") for s in account_Sfollow_list]
    account_Sfollow_list = [s.replace('"', "") for s in account_Sfollow_list]
    
    account_Sfollow_list2 = [s_follow2]
    account_Sfollow_list = [s.replace("[", "") for s in account_Sfollow_list]
    account_Sfollow_list = [s.replace("]", "") for s in account_Sfollow_list]
    account_Sfollow_list = [s.replace('"', "") for s in account_Sfollow_list]
    
    #account_Sall_listに入れていく
    account_Sall_list.append(account_Sfollow_list)
    # account_Sall_list.append(account_Sfollow_list2)
  
    
    for param in account_X_list:
        if param == '':
            account_TL_list.append(param)
        else:
            account_TL_list.append(param)
    # account_TL_list.append(account_X_list)
    #account_X_listをループで一行ずつシートに書き込んでいく
    account_X_df = pd.DataFrame([account_X_list],columns = col)
    account_all_df = pd.concat([account_all_df,account_X_df])
        # print(test_list)
# 'Male'と'Female'をそれぞれ'M'と'F'に置き換える
account_all_df = account_all_df.replace(['\[','"','\]'], '', regex=True)
# TL_list_new_df = pd.DataFrame(TL_list_new)
# TL_list_new_df.to_csv('TL_list_new.csv')



scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('ondemand2-381303-bce643df8a23.json', scope)
client = gspread.authorize(creds)

# スプレッドシートを開く
spreadsheet_name = 'TWダッシュボード'
worksheet_name = 'TWダッシュボード'
sheet = client.open(spreadsheet_name).worksheet(worksheet_name)
# filtered.csvが正しいとすれば、それからスプレッドシートに転記するとうまくいく

sheet.update('DG19', account_all_list)

# スプレッドシートを開く
spreadsheet_name = 'TWダッシュボード'
worksheet_name = 'TWダッシュボード'
sheet = client.open(spreadsheet_name).worksheet(worksheet_name)

sheet.update('CL19',account_Sall_list)

account_TL_df = pd.DataFrame(account_Sall_list)
account_TL_df.to_csv('To_follow_TL.csv')
# print(account_all_df)
account_all_df.to_csv('作業シートY列.csv')
# TL_list_newをXLSX形式にする
# follow_df = pd.DataFrame(TL_list_new)
# print(TL_list_new)


#辞書のキーを抜き出す。
#日付ソートルール
# 最新は月が3月の一番目

# 30日前は1ヶ月前の月
#60日前は2ヶ月前の月の最新

# 文字列を日付に変換
# date_string = "2023/03/8"
# date_string = date_string.split('/')
# date_string = '{}/{}'.format(date_string[0],date_string[1])
# date_obj = datetime.strptime(date_string, "%Y/%m/%d")
# date_obj = datetime.strptime(date_string, "%Y/%m")

# 日付を文字列に変換
# formatted_date = date_obj.strftime("%Y-%m-%d")
# formatted_date = date_obj.strftime("%Y-%m")



# 変換後の日付を表示
# print(formatted_date)
# #日付の差分を計算する
# delta = date_obj - today_datetime
# print(delta.days)
# print(type(delta.days))


# print(GS_master_df)



#スプレッドシートに書き込む場合は、update.cell

# import gspread
# from oauth2client.service_account import ServiceAccountCredentials

# scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
# creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
# client = gspread.authorize(creds)

# # スプレッドシートを開く
# sheet = client.open('スプレッドシート名').worksheet('シート名')
# data = [
#     ['John', 'Doe', 28],
#     ['Jane', 'Doe', 25],
#     ['Bob', 'Smith', 30]
# ]
# sheet.update('A1', data)
# ここで、A1 は書き込みを開始するセルの位置を示します。この例では、A1 から始まって data 配列の内容が書き込まれます。

# 以上の手順に従うと、Google スプレッドシートに一括で書き込むことができます。


    # # スプレッドシートを開く
        # spreadsheet_name = 'TWダッシュボード のコピー'
        # worksheet_name = 'TWダッシュボード'
        # sheet = client.open(spreadsheet_name).worksheet(worksheet_name)
        # sheet.update('BY19:CD19', account_X_list)

        # account_all_list.append(account_X_list)