import math

def circle_area(r:float = 3):
    return math.pi * (r**2)

def square_area(longitud:float):
    sideSize = longitud / 4
    return sideSize ** 2

def triangle_area(base:float, height:float):
    return (base * height) / 2