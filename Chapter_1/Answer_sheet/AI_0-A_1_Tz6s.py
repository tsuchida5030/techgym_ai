import numpy as np

box = np.array([9, 2, 3, 4, 10, 6, 7, 8, 1, 5])

print(f'次元数: {box.ndim}')

print(f'要素数: {box.size}')

print(f'掛け算: {box * box}')

print(f'累乗: {box ** 3}')

print(f'割り算: {box / 2}')

box.sort()
print(f'ソート後: {box}')

box[::-1].sort()
print(f'ソート後: {box}')

print(f'Min: {box.min()}')
print(f'Max: {box.max()}')
print(f'Sum: {box.sum()}')
print(f'Cum: {box.cumsum()}')
print(f'Ratio: {box.cumsum() / box.sum()}')