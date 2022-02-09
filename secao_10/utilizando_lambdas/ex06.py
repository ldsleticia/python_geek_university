# Função Quadrática
# f(x) = a * x ** 2 + b * x + c


def gera_funcao_quadratica(a, b, c):
    return lambda x: a * x**2 + b * x + c


teste = gera_funcao_quadratica(2, 3, -5)

print(teste(0))
print(teste(1))
print(teste(2))
