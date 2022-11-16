#AI-TECHGYM-2-2-A-1
#特徴量エンジニアリング

#インポート
import pandas as pd
import matplotlib.pyplot as plt

#乳がんデータを読み込むためのインポート
from sklearn.datasets import load_breast_cancer

#乳がんデータの取得
cancer = load_breast_cancer()

#データフレーム
df = pd.DataFrame(data=cancer.data , columns=cancer.feature_names)
#display(df)

#カラムを取得
mean_radius = df["mean radius"]

#平均
def mean_KZ(Series):
  a = 0
  for element in Series:
    a += element
  return a / len(Series)
print("平均値",mean_KZ(mean_radius))

#中央値
def median_KZ(Series):
  a1 = Series.max()
  a2 = Series.min()
  return (a1 + a2) / 2
print("中央値",median_KZ(mean_radius))

#最頻値
print("最頻値",mean_radius.mode())

#分散
print("分散",mean_radius.var())

#標準偏差
print("標準偏差",mean_radius.std())

#要約統計量
print("要約統計量",mean_radius.describe())
