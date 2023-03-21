#AI-TECHGYM-2-8-A-2
#特徴量エンジニアリング

#インポート
import pandas as pd
import os
import urllib.request

#ファイルがなければダウンロードする
title = "FIFA_data.csv"
if not os.path.exists(title):
    print(title + " DOWNLOAD.")
    url = "https://raw.githubusercontent.com/amanthedorkknight/fifa18-all-player-statistics/master/2019/data.csv"
    urllib.request.urlretrieve(url,"{0}".format(title))
else :
    print(title + " EXIST.")

df=pd.read_csv('./FIFA_data.csv')

#必要に応じて表示
#display(df.head())

#文字列データの補完
df['Club'].fillna('No Club', inplace = True)
df['Preferred Foot'].fillna('Right', inplace = True)
df['International Reputation'].fillna(1, inplace = True)
df['Weak Foot'].fillna(3, inplace = True)
df['Work Rate'].fillna('Medium/ Medium', inplace = True)
df['Body Type'].fillna('Normal', inplace = True)
df['Position'].fillna('ST', inplace = True)
df['Jersey Number'].fillna(8, inplace = True)
df['Joined'].fillna('Jul 1, 2018', inplace = True)
df['Loaned From'].fillna('None', inplace = True)
df['Contract Valid Until'].fillna(2019, inplace = True)
df['Height'].fillna("5'11", inplace = True)
df['Weight'].fillna('200lbs', inplace = True)
df['Wage'].fillna('€200K', inplace = True)
df['Release Clause'].fillna('€4.2M', inplace = True)

#数値の平均値での補間
df['Crossing'].fillna(df['Crossing'].mean(), inplace = True)
df['Finishing'].fillna(df['Finishing'].mean(), inplace = True)
df['HeadingAccuracy'].fillna(df['HeadingAccuracy'].mean(), inplace = True)
df['ShortPassing'].fillna(df['ShortPassing'].mean(), inplace = True)
df['Volleys'].fillna(df['Volleys'].mean(), inplace = True)
df['Dribbling'].fillna(df['Dribbling'].mean(), inplace = True)
df['Curve'].fillna(df['Curve'].mean(), inplace = True)
df['FKAccuracy'].fillna(df['FKAccuracy'], inplace = True)
df['LongPassing'].fillna(df['LongPassing'].mean(), inplace = True)
df['BallControl'].fillna(df['BallControl'].mean(), inplace = True)
df['Acceleration'].fillna(df['Acceleration'].mean(), inplace = True)
df['SprintSpeed'].fillna(df['SprintSpeed'].mean(), inplace = True)
df['Agility'].fillna(df['Agility'].mean(), inplace = True)
df['Reactions'].fillna(df['Reactions'].mean(), inplace = True)
df['Balance'].fillna(df['Balance'].mean(), inplace = True)
df['ShotPower'].fillna(df['ShotPower'].mean(), inplace = True)
df['Jumping'].fillna(df['Jumping'].mean(), inplace = True)
df['Stamina'].fillna(df['Stamina'].mean(), inplace = True)
df['Strength'].fillna(df['Strength'].mean(), inplace = True)
df['LongShots'].fillna(df['LongShots'].mean(), inplace = True)
df['Aggression'].fillna(df['Aggression'].mean(), inplace = True)
df['Interceptions'].fillna(df['Interceptions'].mean(), inplace = True)
df['Positioning'].fillna(df['Positioning'].mean(), inplace = True)
df['Vision'].fillna(df['Vision'].mean(), inplace = True)
df['Penalties'].fillna(df['Penalties'].mean(), inplace = True)
df['Composure'].fillna(df['Composure'].mean(), inplace = True)
df['Marking'].fillna(df['Marking'].mean(), inplace = True)
df['StandingTackle'].fillna(df['StandingTackle'].mean(), inplace = True)
df['SlidingTackle'].fillna(df['SlidingTackle'].mean(), inplace = True)
df['GKDiving'].fillna(df['GKDiving'].mean(), inplace = True)
df['GKHandling'].fillna(df['GKHandling'].mean(), inplace = True)
df['GKKicking'].fillna(df['GKKicking'].mean(), inplace = True)
df['GKPositioning'].fillna(df['GKPositioning'].mean(), inplace = True)
df['GKReflexes'].fillna(df['GKReflexes'].mean(), inplace = True)

#中央値での補完
df['Skill Moves'].fillna(df['Skill Moves'].median(), inplace = True)

#その他のNaNは0にする
df.fillna(0, inplace = True)

#不要な行を取り除く
df.drop(['Unnamed: 0','Photo','Flag','Club Logo'],axis=1,inplace=True)

df = df.assign(Defending=lambda x: ((x['Marking'] + x['StandingTackle'] + x['SlidingTackle']) / 3))
df = df.assign(General=lambda x: ((x['HeadingAccuracy'] + x['Dribbling'] + x['Curve'] + x['BallControl']) / 4))
df = df.assign(Mental=lambda x: ((x['Aggression'] + x['Interceptions'] + x['Positioning'] + x['Vision'] + x['Composure']) / 5))
df = df.assign(Passing=lambda x: ((x['Crossing'] + x['ShortPassing'] + x['LongPassing']) / 3))
df = df.assign(Mobility=lambda x: ((x['Acceleration'] + x['SprintSpeed'] + x['Agility'] + x['Reactions']) / 4))
df = df.assign(Power=lambda x: ((x['Balance'] + x['Jumping'] + x['Stamina'] + x['Strength']) / 4))
df = df.assign(Rating=lambda x: ((x['Potential'] + x['Overall']) / 2))
df = df.assign(Shooting=lambda x: ((x['Finishing'] + x['Volleys']) + x['FKAccuracy'] + x['ShotPower'] + x['LongShots'] + x['Penalties'] / 6))

defined_columns = ['Defending', 'General', 'Mental', 'Passing', 'Mobility', 'Power', 'Rating', 'Shooting']
df[defined_columns] = df[defined_columns].round()

display(df[defined_columns])