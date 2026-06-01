import numpy as np

a = [3, 4, 5, 6, 7]
b = [7, 8, 12, 20, 100]
c = [8, 100, 200, 13, 255]
d = [10, 20, 30, 40, 50]

# combine_arr = np.array([a, b, c])
# print(combine_arr)
# print(combine_arr.shape)

# re_shape = combine_arr.reshape((5, 3))
# print(re_shape)

new_arr = np.array([a, b, c, d])
number = new_arr.reshape((5, 4))
number = number ** 2
print(number)
print(number[1][1])