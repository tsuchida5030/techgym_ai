#AI-TECHGYM-2-1-Q
#特徴量エンジニアリング

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

sns.displot(data=df, x="mean radius", bins=16, kde=True)
plt.legend()
plt.show()