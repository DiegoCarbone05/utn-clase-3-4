import geometry.calc.area_calc as calc
import geometry.perimeter.calc_perimetro as perimeter
import recursividad.funciones as recursividad

# ----------------------------------------PUNTO 1
circle_area = calc.circle_area(10)
square_area = calc.square_area(20)
triangle_area = calc.triangle_area(10, 30)

print(f"Area de circulo: {circle_area}")
print(f"Area de cuadrado: {square_area}")
print(f"Area de triangulo: {triangle_area}")

# ----------------------------------------PUNTO 2
circle_perimeter = perimeter.perimetro_circulo(10)
square_perimeter = perimeter.perimetro_cuadrado(20)
triangle_perimeter = perimeter.perimetro_triangulo(10)

print(f"Perimetro de circulo: {circle_perimeter}")
print(f"Perimetro de cuadrado: {square_perimeter}")
print(f"Perimetro de triangulo: {triangle_perimeter}")

# ----------------------------------------PUNTO 1
print(recursividad.potencia()) # ejemplo 1
print(recursividad.potencia(3, 4)) # ejemplo 2
print(recursividad.potencia(5, 0)) # ejemplo 3