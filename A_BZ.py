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

#旧と新からコンテナ番号をもらう
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

#dfにいれる　カラム名　userID コンテナ番号
col = [
  'userID',
  'container'
]

old_df = pd.DataFrame(columns = col)

old_df['userID'] = C_column
old_df['container'] = A_column


worksheet_name = 'コンテナB（新）'
sheet = client.open(spreadsheet_name).worksheet(worksheet_name)

# l,k列の値を取得
A_column = sheet.col_values(1)
C_column = sheet.col_values(3)

new_df = pd.DataFrame(columns = col)

new_df['userID'] = C_column
new_df['container'] = A_column





# 今日の日付
today = date.today()
today = today - timedelta(days=3)
today_str = today.strftime("%Y-%m-%d")
print(today_str)
today_str = '2023-03-15'



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

# 60days ago
sixty_days_ago = today - timedelta(days=60)
sixty_days_ago_str = sixty_days_ago.strftime("%Y-%m-%d")

# 90days ago
ninty_days_ago = today - timedelta(days=90)
ninty_days_ago_str = ninty_days_ago.strftime("%Y-%m-%d")

#180day ago
half_a_year_ago = today - timedelta(days=180)
half_a_year_ago_str = half_a_year_ago.strftime("%Y-%m-%d")

#360day ago
a_year_ago = today - timedelta(days=360)
a_year_ago_str = a_year_ago.strftime("%Y-%m-%d")
# A_BT_listのリストを作る
col = [
 'col_A',
 'col_B',
 'col_C',
 'col_D',
 'col_E',
 'col_F',
 'col_G',
 'col_H',
 'col_I',
 'col_J',
 'col_K',
 'col_L',
 'col_M',
 'col_N',
 'col_O',
 'col_P',
 'col_Q',
 'col_R',
 'col_S',
 'col_T',
 'col_U',
 'col_V',
 'col_W',
 'col_Z',
 'col_AA',
 'col_AB',
 'col_AC',
 'col_AD',
 'col_AE',
 'col_AF',
 'col_AG',
 'col_AH',
 'col_AI',
 'col_AJ',
 'col_AK',
 'col_AL',
 'col_AM',
 'col_AN',
 'col_AO',
 'col_AP',
 'col_AQ',
 'col_AR',
 'col_AS',
 'col_AT',
 'col_AU',
 'col_AV',
 'col_AW',
 'col_AX',
 'col_AY',
 'col_AZ',
 'col_BA',
 'col_BB',
 'col_BC',
 'col_BD',
 'col_BE',
 'col_BF',
 'col_BG',
 'col_BH',
 'col_BI',
 'col_BJ',
 'col_BK',
 'col_BL',
 'col_BM',
 'col_BN',
 'col_BO',
 'col_BP',
 'col_BQ',
 'col_BR',
 'col_BS',
 'col_BT',
 'col_BU',
 'col_BV',
 'col_BW',
 'col_BX',
 'col_BY',
 'col_BZ',

]

#shadow_ban セクター
target_filename = 'ターゲット.txt'
#ループの外のリスト
shadow_ban_list = []
target_blanck_list = ['']

# ターゲット.txtをpandasに入れる
target_df = pd.read_csv(target_filename,encoding='cp932')

# ループ用のリスト
# 入力文字
twift_textA = 'twiftA'
twift_textB = 'twiftB'
twift_textC = 'twiftC'
twift_texts = [twift_textB,twift_textA,twift_textC]

#account_dataのリスト
A_account = 'twiftA_account.xlsx'
B_account = 'twiftB_account.xlsx'
C_account = 'twiftC_account.xlsx'
account_list = [B_account,A_account,C_account]

#stat_dataのリスト
A_stat = 'twift_A_unique.xlsx'
B_stat = 'twift_B_unique.xlsx'
C_stat = 'twift_C_unique.xlsx'
stat_list = [B_stat,A_stat,C_stat]
print(len(col))
# account_dfからユーザーIDを抜き出す
# book = xlrd.open_workbook('account-data-2023-03-12.xlsx', encoding_override='utf-8')
#GS update用のリスト
A_BG_list = []
for file_count in range(0,len(account_list),1):
    account_df = pd.read_excel(account_list[file_count])
    account_count = len(account_df)
    #s_dfをユーザーIDと日付で照合して、必要なデータを作っていく
    # book = xlrd.open_workbook('twiftA_uniqe.xlsx', encoding_override='utf-8')

    s_df = pd.read_excel(stat_list[file_count])
    import numpy as np
    s_df['フォロー'] = s_df['フォロー'] .astype(np.int32)
    # for分ここから
    for i in range(0,account_count,1):
        #コンテナ番号のための照合
        container_new_ff = new_df.loc[new_df.iloc[:,0] == account_df.iloc[i,2],:]
        container_old_ff = old_df.loc[old_df.iloc[:,0] == account_df.iloc[i,2],:]
        account_ff = s_df.loc[s_df.iloc[:,2] == account_df.iloc[i,2],:]
        account_ff_today = account_ff.loc[account_ff.iloc[:,4] == today_str]
        account_ff_onedayago = account_ff.loc[account_ff.iloc[:,4] == one_days_ago_str]
        account_ff_twodayago = account_ff.loc[account_ff.iloc[:,4] == two_days_ago_str]
        account_ff_threedayago = account_ff.loc[account_ff.iloc[:,4] == three_days_ago_str]
        account_ff_sevendayago = account_ff.loc[account_ff.iloc[:,4] == seven_days_ago_str]
        account_ff_fourteendayago = account_ff.loc[account_ff.iloc[:,4] == fourteen_days_ago_str]
        account_ff_thirtydayago = account_ff.loc[account_ff.iloc[:,4] == thirty_days_ago_str]
        account_ff_sixtydayago = account_ff.loc[account_ff.iloc[:,4] == sixty_days_ago_str]
        account_ff_nintydayago = account_ff.loc[account_ff.iloc[:,4] == ninty_days_ago_str]
        account_ff_halfyearago = account_ff.loc[account_ff.iloc[:,4] == half_a_year_ago_str]
        account_ff_oneyearago = account_ff.loc[account_ff.iloc[:,4] == a_year_ago_str]
        account_ff_target = target_df.loc[target_df.iloc[:,0] == account_df.iloc[i,2],:]
        
        try:
            status = account_ff_target.iloc[0,1]
        except:
            status = 'エラー'
        # status = [status]
        # shadow_ban_list.extend(status)
        # shadow_ban_list.extend(blanck_list)
        # shadow_ban_list.extend(blanck_list)
        # shadow_ban_list.extend(blanck_list)
        try:
            account_filtered_col_A = str(container_old_ff.iloc[0,1])
        except:
            account_filtered_col_A = '-'
        #作業シートからユーザーIDとコンテナ番号を記入
        try:
            account_filtered_col_B =  str(container_new_ff.iloc[0,1])
        except:
            account_filtered_col_B = '-'
            
        account_filtered_col_C = str(account_ff_today.iloc[0,3])
        # account_filtered_col_A = ''
        account_filtered_col_D = 'https://twitter.com/{}/photo'.format(str(account_ff_today.iloc[0,2]))
        account_filtered_col_E = account_ff_today.iloc[0,2] 
        account_filtered_col_F = twift_texts[file_count]
        account_filtered_col_G = '-'
        account_filtered_col_H = account_ff_today.iloc[0,9]
        account_filtered_col_I = account_ff_today.iloc[0,8]
        # H列：片思い率（フォロアー数÷フォロー数）×100
        try:
            account_filtered_col_J = int(account_filtered_col_H)/int(account_filtered_col_I)*100
            account_filtered_col_J = round(account_filtered_col_J)
        except:
            account_filtered_col_J = 'zero'
        ##lock率
        account_filtered_col_K = '-'
        status_list = account_ff.iloc[:,6]
        #proxy率
        account_filtered_col_L = '-'
        
        
        account_filtered_col_M = status
        
        
        account_filtered_col_X = account_ff_onedayago.iloc[0,9]
        print(account_filtered_col_X)
        #1日前
        account_filtered_col_X = account_ff_onedayago.iloc[0,9]
        #差分
        sabun = account_ff_today.iloc[0,9] - account_ff_onedayago.iloc[0,9]
        account_filtered_col_Y = account_ff_onedayago.iloc[0,8]
        try:
            
            account_filtered_col_Z = int(account_filtered_col_X)/int(account_filtered_col_Y)*100
            account_filtered_col_Z = round(account_filtered_col_Z)
            # account_filtered_col_L = '{}\n{}'.format(account_filtered_col_L,sabun)
            account_filtered_col_AA = '-'
            account_filtered_col_AB = '-'
            account_filtered_col_AC = '-'
        except:
            print('exceptだよ')
            account_filtered_col_X = '-'
            account_filtered_col_Y = '-'
            account_filtered_col_Z = 'zero'

            account_filtered_col_AA = '-'
            account_filtered_col_AB = '-'
            account_filtered_col_AC = '-'
            # account_filtered_col_AA = '-'
        #2日前
        try:
            account_filtered_col_AD = account_ff_twodayago.iloc[0,9]
            #差分
            sabun = account_ff_onedayago.iloc[0,9] - account_ff_twodayago.iloc[0,9]
            account_filtered_col_AE = account_ff_twodayago.iloc[0,8]
            try:
                account_filtered_col_AF = int(account_filtered_col_AD)/int(account_filtered_col_AE)*100
                account_filtered_col_AF = round(account_filtered_col_AF)
            except:
                account_filtered_col_AF = 'zero error'
            # account_filtered_col_R = '{}\n{}'.format(account_filtered_col_R,sabun)
            account_filtered_col_AG = '-'
            account_filtered_col_AH = '-'
            account_filtered_col_AI = '-'
     
        except:
            account_filtered_col_AD = '-'
            #差分
            sabun = '-'
            account_filtered_col_AE = '-'
            account_filtered_col_AF = '-'

            account_filtered_col_AG = '-'
            account_filtered_col_AH = '-'
            account_filtered_col_AI = '-'

        # 3日前
        try:
            account_filtered_col_AJ = account_ff_threedayago.iloc[0,9]
            #差分
            sabun = account_ff_twodayago.iloc[0,9] - account_ff_threedayago.iloc[0,9]
            account_filtered_col_AK = account_ff_threedayago.iloc[0,8]
            try:
                account_filtered_col_AL = int(account_filtered_col_AJ)/int(account_filtered_col_AK)*100
                account_filtered_col_AL = round(account_filtered_col_AL)
            except:
                account_filtered_col_AL = 'zero'
            # account_filtered_col_X = '{}\n{}'.format(account_filtered_col_X,sabun)
            account_filtered_col_AM = '-'
            account_filtered_col_AN = '-'
            account_filtered_col_AO = '-'
        except:
            account_filtered_col_AJ = '-'
            #差分
            sabun = '-'
            account_filtered_col_AK = '-'
            account_filtered_col_AL = '-'

            account_filtered_col_AM = '-'
            account_filtered_col_AN = '-'
            account_filtered_col_AO = '-'
        # 7日前
        try:
            account_filtered_col_AP = account_ff_sevendayago.iloc[0,9]
            #差分
            sabun = account_ff_threedayago.iloc[0,9] - account_ff_sevendayago.iloc[0,9]
            account_filtered_col_AQ = account_ff_sevendayago.iloc[0,8]
            try:
                account_filtered_col_AR = int(account_filtered_col_AP)/int(account_filtered_col_AQ)*100
                account_filtered_col_AR = round(account_filtered_col_AR)
            except:
                account_filtered_col_AR = 'zero error'
            # account_filtered_col_AD = '{}\n{}'.format(account_filtered_col_AD,sabun)
            account_filtered_col_AS = '-'
            account_filtered_col_AT = '-'
            account_filtered_col_AU = '-'

        except:
            account_filtered_col_AP = '-'
            #差分
            sabun = '-'
            account_filtered_col_AQ = '-'
            account_filtered_col_AR = '-'

            account_filtered_col_AS = '-'
            account_filtered_col_AT = '-'
            account_filtered_col_AU = '-'
        # 14日前
        try:
            account_filtered_col_AV = account_ff_fourteendayago.iloc[0,9]
            #差分
            sabun = account_ff_sevendayago.iloc[0,9] - account_ff_fourteendayago.iloc[0,9]
            account_filtered_col_AW = account_ff_fourteendayago.iloc[0,8]
            try:
                account_filtered_col_AX = int(account_filtered_col_AV)/int(account_filtered_col_AW)*100
                account_filtered_col_AX = round(account_filtered_col_AX)
            except:
                account_filtered_col_AX = 'zero error'
            # account_filtered_col_AJ = '{}\n{}'.format(account_filtered_col_AJ,sabun)
            account_filtered_col_AY = '-'
            account_filtered_col_AZ = '-'
            account_filtered_col_BA = '-'

        except:
            account_filtered_col_AV = '-'
            #差分
            sabun = '-'
            account_filtered_col_AW = '-'
            account_filtered_col_AX = '-'

            account_filtered_col_AY = '-'
            account_filtered_col_AZ = '-'
            account_filtered_col_BA = '-'
        # 30日前
        try:
            account_filtered_col_BB = str(account_ff_thirtydayago.iloc[0,9])
            #差分
            sabun = account_ff_today.iloc[0,9] - account_ff_onedayago.iloc[0,9]
            account_filtered_col_BC  = account_ff_thirtydayago.iloc[0,8]
            try:
                account_filtered_col_BD = int(account_filtered_col_BB)/int(account_filtered_col_BC)*100
                account_filtered_col_BD = round(account_filtered_col_BD)
            except:
                account_filtered_col_BD = 'zero error'
            # account_filtered_col_AP  = '{}\n{}'.format(account_filtered_col_AP,sabun)
            account_filtered_col_BE = '-'
            account_filtered_col_BF = '-'
            account_filtered_col_BG = '-'

        except:
            account_filtered_col_BB = '-'
            #差分
            sabun = '-'
            account_filtered_col_BC = '-'
            account_filtered_col_BD = '-'

            account_filtered_col_BE  = '-'
            account_filtered_col_BF = '-'
            account_filtered_col_BG = '-'
        # 60日前
        try:
            account_filtered_col_BH = account_ff_sixtydayago.iloc[0,9]
            #差分
            sabun = account_ff_today.iloc[0,9] - account_ff_onedayago.iloc[0,9]
            account_filtered_col_BI = account_ff_sixtydayago.iloc[0,8]
            try:
                account_filtered_col_BJ = int(account_filtered_col_BH)/int(account_filtered_col_BI)*100
                account_filtered_col_BJ = round(account_filtered_col_BJ)
            except:
                account_filtered_col_BJ = 'zero'
            # account_filtered_col_AV = '{}\n{}'.format(account_filtered_col_AV,sabun)
            account_filtered_col_BK = '-'
            account_filtered_col_BL = '-'
            account_filtered_col_BM = '-'

        except:
            account_filtered_col_BH = '-'
            #差分
            sabun = '-'
            account_filtered_col_BI = '-'
            account_filtered_col_BJ = '-'

            account_filtered_col_BK = '-'
            account_filtered_col_BL = '-'
            account_filtered_col_BM = '-'
        # 90日前
        try:
            account_filtered_col_BN = account_ff_nintydayago.iloc[0,9]
            #差分
            sabun = account_ff_today.iloc[0,9] - account_ff_onedayago.iloc[0,9]
            account_filtered_col_BO = account_ff_nintydayago.iloc[0,8]
            try:
                account_filtered_col_BP = int(account_filtered_col_BN)/int(account_filtered_col_BO)*100
                account_filtered_col_BP = round(account_filtered_col_BP)
            except:
                account_filtered_col_BP = 'zero error'
            # account_filtered_col_BB = '{}\n{}'.format(account_filtered_col_BB,sabun)
            account_filtered_col_BQ = '-'
            account_filtered_col_BR = '-'
            account_filtered_col_BS = '-'

        except:
            account_filtered_col_BN = '-'
            #差分
            sabun = '-'
            account_filtered_col_BO = '-'
            account_filtered_col_BP = '-'

            account_filtered_col_BQ = '-'
            account_filtered_col_BR = '-'
            account_filtered_col_BS = '-'
        # 180日前
        try:
            account_filtered_col_BT = account_ff_halfyearago.iloc[0,9]
            #差分
            sabun = account_ff_today.iloc[0,9] - account_ff_onedayago.iloc[0,9]
            account_filtered_col_BU = account_ff_halfyearago.iloc[0,8]
            try:
                account_filtered_col_BV = int(account_filtered_col_BT)/int(account_filtered_col_BU)*100
                account_filtered_col_BV = round(account_filtered_col_BV)
            except:
                account_filtered_col_BV = 'zero error'
            # account_filtered_col_BH  = '{}\n{}'.format(account_filtered_col_BH,sabun)
            account_filtered_col_BW = '-'
            account_filtered_col_BX = '-'
            account_filtered_col_BY = '-'

        except:
            account_filtered_col_BT = '-'
            #差分
            sabun = '-'
            account_filtered_col_BU = '-'
            account_filtered_col_BV = '-'

            account_filtered_col_BW  = '-'
            account_filtered_col_BX = '-'
            account_filtered_col_BY = '-'
            

        # 360日前
        try:
            account_filtered_col_BZ = account_ff_oneyearago.iloc[0,9]
            #差分
            sabun = account_ff_today.iloc[0,9] - account_ff_onedayago.iloc[0,9]
            account_filtered_col_CA = account_ff_oneyearago.iloc[0,8]
            try:
              account_filtered_col_CB = int(account_filtered_col_BZ)/int(account_filtered_col_CA)*100
              account_filtered_col_CB = round(account_filtered_col_CB)
            except:
              account_filtered_col_CB = 'zero error'
            # account_filtered_col_BN   = '{}\n{}'.format(account_filtered_col_BN,sabun)
            account_filtered_col_CC = '-'
            account_filtered_col_CD = '-'
            account_filtered_col_CE = '-'

        
        except:
            account_filtered_col_BZ = '-'
            #差分
            sabun = ''
            account_filtered_col_CA = '-'
            account_filtered_col_CB = '-'

            account_filtered_col_CC   = '-'
            account_filtered_col_CD = '-'
            account_filtered_col_CE = '-'
        
        
        # NはH-X
        try:
            account_filtered_col_N = int(account_filtered_col_H) - int(account_filtered_col_X)
        except:
            account_filtered_col_N = '-'
        # OはH-AD
        try:
            account_filtered_col_O = int(account_filtered_col_H) - int(account_filtered_col_AD)
        except:
            account_filtered_col_O = '-'
        #PはH-AJ
        
        try:
            account_filtered_col_P = int(account_filtered_col_H) - int(account_filtered_col_AJ)
        except:
            account_filtered_col_P = '-'
        #QはH-AP
        
        try:
            account_filtered_col_Q = int(account_filtered_col_H) - int(account_filtered_col_AP)
        except:
            account_filtered_col_Q = '-'
        #RはH-AV
        
        try:
            account_filtered_col_R = int(account_filtered_col_H) - int(account_filtered_col_AV)
        except:
            account_filtered_col_R = '-'
        #SはH-BB
        try:
            account_filtered_col_S = int(account_filtered_col_H) - int(account_filtered_col_BB)
        except:
            account_filtered_col_S = '-'
        #TはH-BH
        try:
            account_filtered_col_T = int(account_filtered_col_H) - int(account_filtered_col_BH)
        except:
            account_filtered_col_T = '-'
        #UはH-BN
        try:
            account_filtered_col_U = int(account_filtered_col_H) - int(account_filtered_col_BN)
        except:
            account_filtered_col_U = '-'
        #VはH-BT
        try:
            account_filtered_col_V = int(account_filtered_col_H) - int(account_filtered_col_BT)
        except:
            account_filtered_col_V = '-'
        #WはH-BZ
        try:
            account_filtered_col_W = int(account_filtered_col_H) - int(account_filtered_col_BZ)
        except:
            account_filtered_col_W = '-'
        
        
        pre_list = [
                str(account_filtered_col_A),
                str(account_filtered_col_B),
                str(account_filtered_col_C),
                str(account_filtered_col_D),
                str(account_filtered_col_E),
                str(account_filtered_col_F),
                str(account_filtered_col_G),
                str(account_filtered_col_H),
                str(account_filtered_col_I),
                str(account_filtered_col_J),
                str(account_filtered_col_K),
                str(account_filtered_col_L),
                str(account_filtered_col_M),
                str(account_filtered_col_N),
                str(account_filtered_col_O),
                str(account_filtered_col_P),
                str(account_filtered_col_Q),
                str(account_filtered_col_R),
                str(account_filtered_col_S),
                str(account_filtered_col_T),
                str(account_filtered_col_U),
                str(account_filtered_col_V),
                str(account_filtered_col_W),
                str(account_filtered_col_X),
                str(account_filtered_col_Y),
                str(account_filtered_col_Z),
                str(account_filtered_col_AA),
                str(account_filtered_col_AB),
                str(account_filtered_col_AC),
                str(account_filtered_col_AD),
                str(account_filtered_col_AE),
                str(account_filtered_col_AF),
                str(account_filtered_col_AG),
                str(account_filtered_col_AH),
                str(account_filtered_col_AI),
                str(account_filtered_col_AJ),
                str(account_filtered_col_AK),
                str(account_filtered_col_AL),
                str(account_filtered_col_AM),
                str(account_filtered_col_AN),
                str(account_filtered_col_AO),
                str(account_filtered_col_AP),
                str(account_filtered_col_AQ),
                str(account_filtered_col_AR),
                str(account_filtered_col_AS),
                str(account_filtered_col_AT),
                str(account_filtered_col_AU),
                str(account_filtered_col_AV),
                str(account_filtered_col_AW),
                str(account_filtered_col_AX),
                str(account_filtered_col_AY),
                str(account_filtered_col_AZ),
                str(account_filtered_col_BA),
                str(account_filtered_col_BB),
                str(account_filtered_col_BC),
                str(account_filtered_col_BD),
                str(account_filtered_col_BE),
                str(account_filtered_col_BF),
                str(account_filtered_col_BG),
                str(account_filtered_col_BH),
                str(account_filtered_col_BI),
                str(account_filtered_col_BJ),
                str(account_filtered_col_BK),
                str(account_filtered_col_BL),
                str(account_filtered_col_BM),
                str(account_filtered_col_BN),
                str(account_filtered_col_BO),
                str(account_filtered_col_BP),
                str(account_filtered_col_BQ),
                str(account_filtered_col_BR),
                str(account_filtered_col_BS),
                str(account_filtered_col_BT),
                str(account_filtered_col_BU),
                str(account_filtered_col_BV),
                str(account_filtered_col_BW),
                str(account_filtered_col_BX),
                str(account_filtered_col_BY),
                str(account_filtered_col_BZ),
                str(account_filtered_col_CA),
                str(account_filtered_col_CB),
                str(account_filtered_col_CC),
                str(account_filtered_col_CD),
                str(account_filtered_col_CE),
            ]
        print(pre_list)
        for param in pre_list:
            param.replace("'",'')
        #int64をint型に 
        # new_list = []
        # for s in pre_list:
        #     new_list.append(s.decode('utf-8', errors='ignore'))


        
        print('pre_listの数は{}'.format(len(pre_list)))
        A_BG_list.append(pre_list)
      

# print(A_BG_list)
#csvにupdate
# A_BG_list_str = [str(x) for x in A_BG_list] 
# スプレッドシートを開く
spreadsheet_name = 'TWダッシュボード'
worksheet_name = 'TWダッシュボード'
sheet = client.open(spreadsheet_name).worksheet(worksheet_name)
sheet.update('A19', A_BG_list)

# # DataFrameオブジェクトを作成
# df = pd.DataFrame([A_BG_list])

# # Excelファイルに書き込み
# df.to_excel('output.xlsx', index=False)