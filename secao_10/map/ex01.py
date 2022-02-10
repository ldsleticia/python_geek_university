import math

# Função 
def area(r):
    return math.pi * (r ** 2)

# Iterável
raios = [2, 5, 7.1, 0.3, 10, 44]


# Forma sem o Map
areas = []
for r in raios:
    areas.append((area(r)))
print(areas)


# Utilizando o Map
areas = map(area, raios)
print(list(areas))

# Utlizando Map com Lambda
print(list(map(lambda r: math.pi * (r ** 2), raios)))