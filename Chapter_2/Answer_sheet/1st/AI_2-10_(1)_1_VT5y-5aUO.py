#AI-TECHGYM-2-10-Q
#特徴量エンジニアリング

# 実行場所
import os
os.chdir(r"C:\Users\tsuchida\Documents\techgym_セミナー\TortoiseGit_resorce\techgym_ai\Chapter_2\Answer_sheet\AI_Chapter2_saved_files")

#インポート
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import os

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
    
selected_columns = ['Name', 'Age', 'Nationality', 'Overall', 'Potential', 'Club', 'Value',
                    'Wage', 'Special', 'Preferred Foot', 'International Reputation', 'Weak Foot',
                    'Skill Moves', 'Work Rate', 'Body Type', 'Position', 'Height', 'Weight',
                    'Finishing', 'HeadingAccuracy', 'ShortPassing', 'Volleys', 'Dribbling',
                    'Curve', 'FKAccuracy', 'LongPassing', 'BallControl', 'Acceleration',
                    'SprintSpeed', 'Agility', 'Reactions', 'Balance', 'ShotPower',
                    'Jumping', 'Stamina', 'Strength', 'LongShots', 'Aggression',
                    'Interceptions', 'Positioning', 'Vision', 'Penalties', 'Composure',
                    'Marking', 'StandingTackle', 'SlidingTackle', 'GKDiving', 'GKHandling',
                    'GKKicking', 'GKPositioning', 'GKReflexes', 'Release Clause']
#データフレーム
data_selected = pd.DataFrame(df, columns = selected_columns)

#相関係数のヒートマップ
plt.figure(figsize=(20,20))
sns.heatmap(data_selected.corr(), linewidths=0.1, linecolor='black', square=True, cmap='summer')
plt.title('Heatmap of the dataset')
plt.show()

#年齢とレーティングの関係
plt.figure(figsize = (15,5))
sns.lineplot(data=df, x='Age', y='Rating', palette = 'Wistia')
plt.title('Age vs Rating', fontsize = 20)
plt.show()

#上位9ヶ国の選手の体重の分布

#クラブ別の総合値の分布

#年齢とポテンシャルの分布