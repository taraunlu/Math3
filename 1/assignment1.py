
import math
from tabulate import tabulate

# tehtava 1 a)

asteet = math.degrees(2.493)
print(f"Tehtävä 1. a) {int(asteet)}°")

# 1 b)

asteet = math.degrees(0.911)
print(f"Tehtävä 1. b) {int(asteet)}°")

# tehtava 2 a)

asteet = math.radians(137.7)
print(f"Tehtävä 2. a) {asteet:.3f} rad")

# tehtava 2 b)

asteet = math.radians(62.3)
print(f"Tehtävä 2. b) {asteet:.3f} rad")


# tehtava 3

print("Tehtävä 3.")
table = [['°', 'Rad'],
         ['30', round(math.radians(30), 3)],
         ['45', round(math.radians(45), 3)],
         ['60', round(math.radians(60), 3)],
         ['90', round(math.radians(90), 3)],
         ['120', round(math.radians(120), 3)],
         ['135', round(math.radians(135), 3)],
         ['150', round(math.radians(150), 3)],
         ['180', round(math.radians(180), 3)],
         ['270', round(math.radians(270), 3)],
         ['360', round(math.radians(360), 3)]]


print(tabulate(table))



