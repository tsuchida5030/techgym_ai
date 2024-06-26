#AI-TECHGYM-N-C1
import numpy as np
import scipy.linalg as linalg

matrix = np.array([[1,-1,-1], [-1,1,-1], [-1,-1,1]])
display(matrix)

# 行列式
display('行列式')
display(linalg.det(matrix))

# 逆行列
display('逆行列')
display(linalg.inv(matrix))
display(np.dot(matrix, linalg.inv(matrix)))


# 固有値と固有ベクトル
eig_value, eig_vector = linalg.eig(matrix)

# 固有値と固有ベクトル
display('固有値')
display(eig_value)
display('固有ベクトル')
display(eig_vector)