#AI-TECHGYM-2-11-A-1
#特徴量エンジニアリング

#インポート
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import os
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error

# 実行場所
import os
os.chdir(r"C:\Users\tsuchida\Documents\techgym_セミナー\TortoiseGit_resorce\techgym_ai\Chapter_2\Answer_sheet\AI_Chapter2_saved_files")

#ファイルがなければ前の問題を実施する
title = "FIFA_data_pre2.csv"
if not os.path.exists(title):
    print("Run Previous problem.")
else :
    print(title + " EXIST.")
    df=pd.read_csv('./FIFA_data_pre2.csv')

#スタイル指定
plt.style.use('fivethirtyeight')
sns.set(style = "dark", palette = "colorblind", color_codes = True)

#不要な列を削除する
drop_cols = df.columns[28:54]
df = df.drop(drop_cols, axis = 1)
df = df.drop(['Unnamed: 0','Unnamed: 0.1','ID','Jersey Number','Joined','Loaned From',
              'Body Type', 'Release Clause','Contract Valid Until','LS','ST',
              'Value','Name','Club'], axis = 1)

df[df['Real Face'] == 'Yes']
df['Real Face'] == 'Yes'


ls_GK = ['GK']
ls_DF = ['RB','LB','CB','LCB','RCB','RWB','LWB']
ls_DM = ['LDM', 'CDM', 'RDM']
ls_MF = ['LM', 'LCM', 'CM', 'RCM', 'RM']
ls_AM = ['LAM', 'CAM', 'RAM', 'LW', 'RW']
ls_ST = ['RS', 'ST', 'LS', 'CF', 'LF', 'RF']

# ls_GK = ['GK',['GK']]
# ls_DF = ['DF',['RB','LB','CB','LCB','RCB','RWB','LWB']]
# ls_DM = ['DM',['LDM', 'CDM', 'RDM']]
# ls_MF = ['LM', 'LCM', 'CM', 'RCM', 'RM']
# ls_AM = ['LAM', 'CAM', 'RAM', 'LW', 'RW']
# ls_ST = ['RS', 'ST', 'LS', 'CF', 'LF', 'RF']
# dict_position = {
#     'GK' : 'GK',
#     'RB' : 'DF', 'LB' : 'DF', 'LB' : 'DF',
# }
# def make_dict(ls):
#     for element in ls:
#         dict_position

def check_position(x):
    # return dict_positon[x] ・・・ 辞書型をキーで指定する書き方もあったはず
    if x in ls_GK:
        return 'GK'
    elif x in ls_DF:
        return 'DF'
    elif x in ls_DM:
        return 'DM'
    elif x in ls_MF:
        return 'MF'
    elif x in ls_AM:
        return 'AM'
    elif x in ls_ST:
        return 'ST'
    else:
        print('!例外! ' + x + '：該当ポジションが見つかりません')

df['Category_Real Face'] = df['Real Face'].apply(
    lambda x: 0 if x == 'No' else 1)

df['Category_Preferred Foot'] = df['Preferred Foot'].apply(
    lambda x: 0 if x == 'Left' else 1)

df['Simple_Position'] = df['Position'].apply(
    lambda x: check_position(x))

Football_players_count = df['Nationality'].value_counts()
df['Category_Nationality'] = df['Nationality'].apply(
    lambda x: 0 if Football_players_count[x] <= 250 else 1)

df['Work Rate1'] = df['Work Rate'].apply(
    lambda x: x.split('/')[0])

df['Work Rate2'] = df['Work Rate'].apply(
    lambda x: x.split('/')[1])

df['feet'] = df['Height'].apply(
    lambda x: float(x.split('\'')[0]))

df['inch'] = df['Height'].apply(
    lambda x: float(x.split('\'')[1]))
    
df['Height_cm'] = df['feet'] * 30.48 + df['inch'] * 2.54
# display(df.head())

obj_list = ['Real Face', 'Preferred Foot', 'Position', 'Nationality', 'Work Rate', 'Height', 'feet', 'inch']
df.drop(obj_list, axis=1, inplace=True)
# display(df[obj_list])
# display(df)

#カテゴリ変数となる項目名が一列目に縦に並ぶデータフレームに対して、ワンホットエンコーディングを実行し、カテゴリ変数に対して0／1が入った行列を作る
df_c = pd.get_dummies(df)
# Category_parameters = ['Simple_Position', 'Work Rate1', 'Work Rate2']
# df_c = pd.get_dummies(df[Category_parameters])
# df = pd.concat([df, df_c], axis=1)
# display(df_c)
# df.drop(Category_parameters, axis=1, inplace=True)
# display(df_c)

#作成した特徴量
df_p = df_c

target = df_p['Overall']
df_t = df_p.drop(['Overall'], axis = 1)
X_train, X_test, y_train, y_test = train_test_split(df_t, target, test_size=0.2)

model = LinearRegression()
model.fit(X_train, y_train)
predictions = model.predict(X_test)

#結果の表示
print('決定係数(train):{:.3f}'.format(model.score(X_train,y_train)))
print('決定係数(test):{:.3f}'.format(model.score(X_test,y_test)))
print('RMSE :{:.3f} '.format(np.sqrt(mean_squared_error(y_test, predictions))))

df_test = pd.DataFrame({'Overall':y_test,'Predictions':predictions})
# display(df_test)
sns.regplot(x="Predictions", y="Overall", data=df_test, scatter_kws={'alpha':0.3,'color':'lime'}, line_kws={'alpha':0.5, 'color':'b'})