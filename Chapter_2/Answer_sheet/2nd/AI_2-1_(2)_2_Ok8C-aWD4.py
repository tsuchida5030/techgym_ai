#AI-TECHGYM-2-1-Q
#特徴量エンジニアリング

# 作業場所
import os
os.chdir(r"C:\Users\tsuchida\Documents\techgym_セミナー\tortoisegit\techgym_ai\Chapter_2\Answer_sheet\AI_Chapter2_saved_files")

#インポート
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns

#乳がんデータを読み込むためのインポート
from sklearn.datasets import load_breast_cancer

#乳がんデータの取得
cancer = load_breast_cancer()

#データフレーム
df = pd.DataFrame(data=cancer.data , columns=cancer.feature_names)

sns.set()
sns.set_style('whitegrid')

sns.displot(data=df, x="mean radius", bins=16, kde=True, legend=True)
plt.show()