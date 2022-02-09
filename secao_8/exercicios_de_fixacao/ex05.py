import math

def calcula_volume(raio):
    # V= 4/3*pi*r^3
    volume = 4/3 * math.pi * math.pow(float(raio),3)
    return (f'O volume da esfera passada é de {volume}')

print(calcula_volume(2))