# # a = 5
# # b = 10
# # a,b = b,a
# # print(a , b)
# a = "Data"
# b = "Science"

# print(a + "-" + b)
# print("-".join([a, b]))
import numpy as np
# a = np.array([[1,2], [3,4]])
# b = np.array([[5,6], [7,8]])
# c = np.dot(a, b)
# print(c)
# a = np.arange(10)
# print(a)
# b = a[1:5]#0,1,2,3,4,5,6,7,8,9
# print(b)
# b[0] = 10
# print(a)
# s = {1,2,3,4}
# l = []
# for i in range(len(s)):
#     l += [1+i]
# # print(l)
# a = {1,'two',3.0,3,27.5,'four',5}
# b = {27.5,10}
# print(a|b)  # Union of sets
a = np.array([range(i, i+4) for i in [1,3,5]])
print(a)