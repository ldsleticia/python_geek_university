def conta_ate(valor_maximo):
    contador = 1
    while contador <= valor_maximo:
        yield contador
        contador = contador + 1


gen = conta_ate(5)
print(type(gen))
print(
    next(gen)
)  # Funciona somente ao colocar tantos nexts quanto elementos solicitados ou utilizando o for
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

gen = conta_ate(10)
for num in gen:
    print(num)
