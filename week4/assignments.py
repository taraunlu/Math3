from sympy import solve
from sympy.abc import x, y, z


# OSA 2

# TEHTÄVÄ 1 a)

vastaus = solve([x - 2*y - 2*z, -2*x + y - z + 3, 3*x + 2*y + z - 4], [x, y, z], dict=True)
print(f"Tehtävä 1a) {vastaus}")

# TEHTÄVÄ 1 b)

vastaus = solve([x + y - 1, 2*x + y - z - 1, 3*x + y - 2*z - 1], [x, y, z], dict=True)
print(f"Tehtävä 1b) {vastaus}")

# TEHTÄVÄ 2 a)

vastaus = solve([2*x + 4*y - z - 11, 6*x - y - 3*z - 7, 4*x + 5*y - 2*z - 16], [x, y, z], dict=True)
print(f"Tehtävä 2a) {vastaus}")

# TEHTÄVÄ 2 b)

vastaus = solve([4*x + 2*y - 2*z, 2*x + y - z - 1, 3*x + y - 2*z - 1], [x, y, z], dict=True)
print(f"Tehtävä 2b) {vastaus}")


# OSA 3
# TEHTÄVÄ 1 a)

vastaus = solve([5*x + 3*y - 9, 2*x + y - 4], [x, y], dict=True)
print(f"Tehtävä 1a) {vastaus}")

# TEHTÄVÄ 1 b)

vastaus = solve([2*x + y + z - 6, x + 3*y + z - 2, 2*x + y + 2*z - 9], [x, y, z], dict=True)
print(f"Tehtävä 1b) {vastaus}")


# TEHTÄVÄ 1 c)

vastaus = solve([x + y + 3*z + 1, 3*x + y + z - 5, 2*x + y + 2*z - 2], [x, y, z], dict=True)
print(f"Tehtävä 1c) {vastaus}")

