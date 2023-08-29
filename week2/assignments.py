import numpy as np

# TEHTÄVÄ 1
# Määrittele ja esitä 5-alkioinen kokonaislukutaulukko numpyn avulla.
# luvut voivat olla satunnaisia.


# Luo 5-alkioinen kokonaislukutaulukko satunnaisilla luvuilla
array = np.random.randint(1, 10, size=5)

print(array)


# TEHTÄVÄ 2
# Sinulla on vektorit a) u = 2i + 3j, v =4i - 7j
# b) uu= i + j + k, vv 3i -3j + 2k.
# Määrittele nämä numpy taulukon avulla.

# 2a)
# Luo vektorit u ja v Numpy taulukon avulla
u = np.array([2, 3])
v = np.array([4, -7])

# Tulosta vektorit u ja v
print("Vektori u:", u)
print("Vektori v:", v)

# 2 b)
# Luo vektorit u ja v Numpy taulukon avulla
uu = np.array([1, 1, 1])
vv = np.array([3, -3, 2])

# Tulosta vektorit uu ja vv
print("Vektori uu:", uu)
print("Vektori vv:", vv)


# TEHTÄVÄ 3
# Laske kunkin vektorin normi.

# Laske vektorin u normi
u_norm = np.linalg.norm(u)
print(f"Vektorin u normi: {u_norm:.2f}")

# Laske vektorin v normi
v_norm = np.linalg.norm(v)
print(f"Vektorin v normi: {v_norm:.2f}")

# Laske vektorin uu normi
uu_norm = np.linalg.norm(uu)
print(f"Vektorin uu normi: {uu_norm:.2f}")

# Laske vektorin vv normi
vv_norm = np.linalg.norm(vv)
print(f"Vektorin vv normi: {vv_norm:.2f}")