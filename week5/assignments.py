import numpy as np


# TEHTÄVÄ 4 PYTHON-OSUUS TEHT. 1

# 1a)
m1 = np.array([[-1, 2], [3, 1]])
m2 = np.array([[0, 1, 3], [2, -3, 5]])
m3 = np.dot(m1, m2)
print("Tehtävä 1. 1a)")
print(m3)

# 1b)
m1 = np.array([[1, 3, 5], [0, -2, 1], [2, -1, 4]])
m2 = np.array([[1], [-3], [-1]])
m3 = np.dot(m1, m2)
print("Tehtävä 1. 1b)")
print(m3)

# 1c)
m1 = np.array([[2, 0, 1], [1, -3, 4], [0, 1, 5]])
m2 = np.array([[3], [-5], [7]])
m3 = np.dot(m1, m2)
print("Tehtävä 1. 1c)")
print(m3)

# 1d)
m1 = np.array([[1, -4, 2], [3, 0, -2], [2, 1, 0]])
m2 = np.array([[5, 1, -1], [-2, 1, 3], [0, 3, 4]])
m3 = np.dot(m1, m2)
print("Tehtävä 1. 1d)")
print(m3)


# TEHTÄVÄ 4 PYTHON-OSUUS: TEHT.2 TRANSPOOSIT JA DETERMINANTIT

# TEHTÄVÄ 1
# A
a = np.array([[4, 9, 0], [-3, 7, -11]])
print("Transpoosi tehtävä 1. A")
print(np.transpose(a))

# B
a = np.array([[8, 9], [-3, 12], [0, -1], [7, 1]])
print("Transpoosi tehtävä 1. B")
print(np.transpose(a))

# TEHTÄVÄ 2
# 1a)
a = np.array([[5, -6], [8, 10]])
print("Determinantti tehtävä 2. 1a)")
print(f"{np.linalg.det(a):.0f}")

# 1b)
x = 1
a = np.array([[1-x, -x], [x, 1-x]])
print("Determinantti tehtävä 2. 1b)")
print(f"{np.linalg.det(a):.0f}")

# 2a)
a = np.array([[2, 3, 4], [-2, -1, 1], [5, 3, 2]])
print("Determinantti tehtävä 2. 2a)")
print(f"{np.linalg.det(a):.0f}")

# 2b)
a = np.array([[3, 15, 7], [0, -4, 0], [3, 2, 3]])
print("Determinantti tehtävä 2. 2b)")
print(f"{np.linalg.det(a):.0f}")

# TEHTÄVÄ 3

# 1)
a = np.array([[-2, 0, 8, 5], [3, -1, 2, 1], [4, 7, 6, 2], [1, 0, 2, 3]])
print("Determinantti tehtävä 3. 1)")
print(f"{np.linalg.det(a):.0f}")
