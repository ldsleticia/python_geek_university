from functools import reduce

dados = [2, 3, 4, 5, 7, 11, 13, 17, 19, 23, 29]

multi = lambda x, y: x * y
res = reduce(multi, dados)
print(res)

resultado = 1
for n in dados:
    resultado = resultado * n
print(res)
