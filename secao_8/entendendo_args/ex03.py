def soma_numeros(*args):
    return sum(args)


# TypeError
# numeros = [1, 2, 3, 4, 5, 6, 7]
# print(soma_numeros(numeros))

# Desempacotador automático
# Ao colocar o * na frente, o Python entende que deve desempacotar os dados antes de usar
# Não funciona com dicionário pois ele trabalha com o conceito chave/valor
numeros = [1, 2, 3, 4, 5, 6, 7]
print(soma_numeros(*numeros))
