import math

def circle_states(radius):
    area = math.pi * radius **2
    circumference = math.pi * radius
    return area, circumference

a,c = circle_states(3)

print("area", a, "circumference", c)