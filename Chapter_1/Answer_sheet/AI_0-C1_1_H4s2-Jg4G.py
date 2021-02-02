#AI-TECHGYM-N-C1
import numpy as np
import scipy.linalg as linalg

matrix = np.array([[1,-1,-1], [-1,1,-1], [-1,-1,1]])
display(matrix)

# 行列式
det_matrix = linalg.det(matrix)
display('行列式')
display(det_matrix)


# 逆行列
invers_matrix = linalg.inv(matrix)
display('逆行列')
display(invers_matrix)




# 固有値と固有ベクトル
eig_value, eig_vector = linalg.eig(matrix)
eig_vector = np.round(eig_vector, 2)

# 固有値と固有ベクトル
display('固有値')
display(eig_value)
display('固有ベクトル')
display(eig_vector)