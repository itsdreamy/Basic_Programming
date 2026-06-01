import numpy as np

list_1 = [11, 12, 13, 14]
list_2 = [1, 2, 3, 4]
list_3 = [21, 22, 23, 24,]
arr = np.array([list_1, list_2, list_3])
new = arr.reshape(6, 2)
print(new)