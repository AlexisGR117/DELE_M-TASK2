"""Calculate where the function f(x)=x^3+3 passes through axis X using Newtons Method"""

def calculate_Newton_Root():
  value = -2
  difference = 1
  predefined_error = 0.000000000000000001
  while (difference > predefined_error):
    initial_value = value
    value = value - (value**3 + 3) / (3*value**2)
    difference = abs(initial_value - value)
    print(f"Initial Value: {initial_value}, Value: {value}, Difference: {difference}")
  return value
