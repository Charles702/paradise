#----------------------------------------
import numpy as np
import math


A = np.random.randn(4,3)
B = np.sum(A, axis = 1, keepdims = True)
print(A)
print(B)

a = np.random.randn(3,3)
b = np.random.randn(3,1)
print(a*b)

c = np.array([[2,2,2],[3,3,3],[1,1,1],[4,4,4]])
d = np.array([[2],[2],[2],[2]])
print(c)
print(d)
print(c+d)


s = 1 / (1 + math.exp((-1) * 3))
print(s)

w = np.array([4,5,6])
print(1/np.exp(w))

