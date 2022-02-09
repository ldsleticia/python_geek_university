import math

def calcula_hipotenusa(a, b):
    hipotenusa = (a ** 2 + b ** 2) ** (1/2)
    return hipotenusa

print(calcula_hipotenusa(1, 2))
print(math.hypot(1, 2))