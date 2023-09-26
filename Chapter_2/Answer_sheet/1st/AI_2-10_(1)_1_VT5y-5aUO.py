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
# major_countries = list(df['Nationality'].value_counts().index[0:9])
# top9_countries_WofP = []
# for country in major_countries:
#     top9_countries_WofP.append(np.array(df[df['Nationality']==country].Weight))
# # print(major_countries[0])
# # display(top9_countries_WofP[0])
# fig = plt.figure(figsize = (15,5))
# ax = fig.add_subplot(1, 1, 1)
# ax.violinplot(top9_countries_WofP)
# ax.set_xticklabels(major_countries)
# ax.set_xlabel('Countries')
# ax.set_ylabel('Weight in lbs')
# ax.set_title('Distribution of Weight of players from different countries')
# plt.show()

#上位9ヶ国の選手の体重の分布
some_countries = ['England','Germany','Spain','Argentina','France','Brazil','Italy','Columbia','Japan']
data_countries = df.loc[df['Nationality'].isin(some_countries)]
plt.figure(figsize = (15,5))
ax = sns.violinplot(x = data_countries['Nationality'], y = data_countries['Weight'], palette = 'Blues')
ax.set_xlabel(xlabel = 'Countries', fontsize = 16)
ax.set_ylabel(ylabel = 'Weight in lbs', fontsize = 16)
ax.set_title(label = 'Distribution of Weight of players from different countries', fontsize = 20)
plt.show()

#クラブ別の総合値の分布
some_popular_clubs = ['Chelsea', 'Real Madrid', 'FC Barcelona', 'Tottenham Hotspur', 'Valencia CF', 'Southampton', 'RC Celta', 'CD Leganés', 'Empoli', 'Fortuna Düsseldorf']
data_clubs = df.loc[df['Club'].isin(some_popular_clubs)]
plt.figure(figsize = (15,5))
ax = sns.boxplot(x = 'Club', y = 'Overall', data = data_clubs, palette = 'inferno')
ax.set_xlabel(xlabel = 'Some Popular Clubs', fontsize = 16)
ax.set_ylabel(ylabel = 'Overall Score', fontsize = 16)
ax.set_title(label = 'Distribution of Overall Score in Different popular Clubs', fontsize = 20)
plt.show()

#年齢とポテンシャルの分布
ax = sns.jointplot(x = 'Age', y = 'Potential', data = df, joint_kws = {'alpha':0.1,'s':5,'color':'green'},marginal_kws = {'color':'green'},height=8)
plt.show()