"""
Calculate the area under the curve f(x) = x^2, between a=2,b=3. Use the sum of areas under the curve.
"""

def calculate_area(num_subintervals) :
    width_rectangle = 1 / num_subintervals
    area = 0.0
    for subinterval in range(num_subintervals) :
        midpoint = 2 + subinterval * width_rectangle
        height_rectangle = midpoint ** 2
        area += height_rectangle * width_rectangle
    return area

num_subintervals = int(input("Ingrese el valor de n-subintervalos: "))
area_first_function = calculate_area(num_subintervals)
print(f"Aproximación de la integral de la primer función: {area_first_function}")
