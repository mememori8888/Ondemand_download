import pandas as pd
from datetime import datetime,date,timedelta
import gspread
from oauth2client.service_account import ServiceAccountCredentials

#スプレッドシートの色塗りK,L列からユーザー名取得

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('ondemand2-381303-bce643df8a23.json', scope)
client = gspread.authorize(creds)

# スプレッドシートを開く
spreadsheet_name = '作業シート　運用版②'
worksheet_name = 'コンテナA（旧）'
sheet = client.open(spreadsheet_name).worksheet(worksheet_name)



# l,k列の値を取得
A_column = sheet.col_values(1)
C_column = sheet.col_values(3)

print(A_column)
print(C_column)

#dfにいれる　カラム名　userID コンテナ番号
col = [
  'userID',
  'container'
]

old_df = pd.DataFrame(columns = col)

old_df['userID'] = C_column
old_df['container'] = A_column

print(old_df)

worksheet_name = 'コンテナB（新）'
sheet = client.open(spreadsheet_name).worksheet(worksheet_name)

# l,k列の値を取得
A_column = sheet.col_values(1)
C_column = sheet.col_values(3)

print(A_column)
print(C_column)

#dfにいれる　カラム名　userID コンテナ番号
col = [
  'userID',
  'container'
]

new_df = pd.DataFrame(columns = col)

new_df['userID'] = C_column
new_df['container'] = A_column

print(new_df)

#これらをTWダッシュボードのAB列に分けていれる IDで照合する　プログラムはA_BS.pyを改修する。
# 先にcol_Aをcol_Cにずらして、CからM列までにリストを分割して、入力する。その他のリストはX列からBZ列に入れる。その他のファイルもupdate先を変える


#分けていれたあと、列のずれを回収する。col_A ⇒　col_Cという具合
# 対象ファイル A_BS.py  ⇒　A_BZ.py
#              CT_CZ.py ⇒ DG_DM.py
#              CB_CI_TEST.py ⇒ CO_CV.py
#              CL_CR.py ⇒ CX_DE.py
#              TL.py ⇒ TL.py


