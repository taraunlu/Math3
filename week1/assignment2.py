
import math

x = 2.3
y = 4.7

hypotenuusa = math.hypot(x, y)

kulma1 = math.degrees(math.asin(y / hypotenuusa))
kulma2 = 180 - 90 - 63.9

print(f"Hypotenuusan pituus: {hypotenuusa:.1f}")
print(f"Kaksi muuta kulmaa: {kulma1:.1f}° ja {kulma2:.1f}°")



