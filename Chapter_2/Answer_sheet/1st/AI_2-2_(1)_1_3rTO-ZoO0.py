#AI-TECHGYM-2-2-Q
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

mean_radius = df['mean radius']

print('平均値：{}'.format(mean_radius.mean()))
print('最頻値：{}'.format(mean_radius.))