# coding: utf-8
import numpy as np
#
# A = {"A": 1, "B": 2}
# print(list(A.keys()))
# A = [[1865, 7038, 1], [252, 251, 0], [360, 376, 1], [360, 388, 1], [360, 392, 1], [360, 397, 1], [360, 398, 1], [360, 404, 1]]
# # A = []
# B = []
# B.append(1865)
# B.append(7038)
# B.append(1)
# print(np.array(B).shape)
# # A.append(B)
# # B = []
# # B.append(252)
# # B.append(251)
# # B.append(0)
# # A.append(B)
# # print(A)
# A = np.array(A)
# print(A.shape)
# print(A[:, :1])
# print(A[:, :1].flatten().shape)
# print("------")
# print(A[:, 1:2])
# print("------")
# print(A[:, 2:3])
# print("------")
# print([A[:, :1], A[:, 1:2]])

a = np.random.randn(4, 3)
b = np.random.randn(3, 2)
# c = a * b
c = np.dot(a, b)
print(c.shape)

