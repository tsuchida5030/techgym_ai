#AI-TECHGYM-2-3-A-2
#特徴量エンジニアリング

#インポート
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#乳がんデータを読み込むためのインポート
from sklearn.datasets import load_breast_cancer

#乳がんデータの取得
cancer = load_breast_cancer()

#データフレーム
df = pd.DataFrame(data=cancer.data , columns=cancer.feature_names)

#カラムを取得
mean_radius = df["mean radius"]

#NaNを挿入する場所
nan_list = np.random.randint(0,len(mean_radius),30)

#欠損値を埋め込み
for nan in nan_list:
    df.iloc[nan,0] = np.nan

#欠損値の確認
#print("欠損値の数",mean_radius.isnull().sum())
#print("データの数",len(mean_radius))
#print("平均値",mean_radius.mean())

#平均値から標準偏差でばらつきを考慮して補完
#正規分布に従うとし、標準偏差の範囲内でランダムに数字を作る
age_p = mean_radius.mean() - mean_radius.std()
age_m = mean_radius.mean() + mean_radius.std()
age_nc = mean_radius.isnull().sum() #null値の数＝補完する数
rand = np.random.randint(age_p, age_m, size = age_nc)

#欠損値の補完
df_c = df.copy()
df_c["mean radius"][np.isnan(df_c["mean radius"])] = 1

#カラムを取得
mean_radius_c = df_c["mean radius"]

#補完値で置き換え
print("補完値に置き換え後：'1'の数",mean_radius_c[mean_radius_c==1].sum())
print("補完値に置き換え後：欠損値の数",df["mean radius"].isnull().sum())

df_c["mean radius"][df_c["mean radius"]!=1] = 0

#補完値で置き換え
print("補完値に置き換え後：'0'の数",df_c["mean radius"][df_c["mean radius"]==0].sum())