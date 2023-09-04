import numpy as np

# TEHTÄVÄ 4

# 1

A = np.array([[-1, 2], [3, -5]])
B = np.array([[2, 0], [-1, 4]])


tulo = (2 * A + 3 * B)

erotus = (A - B)

print(tulo)
print(erotus)

# 2

A2 = np.array([[2, 3, 1], [0, 7, -2]])

for i in range(1, 3):
    for j in range(1, 4):
        A2[i-1][j-1] = A2[i-1][j-1] * (1+i)

print(A2)



