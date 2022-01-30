# Definindo conjuntos

# Forma 1
s = set({1 , 2, 3, 4, 5, 5, 6, 7, 2, 3})
print(s)
print(type(s))

#Forma 2
s = {1, 2, 3, 4, 5, 5}
print(s)
print(type(s))
print()


#Verificar se há determinado valor no conjunto
if 3 in s:
    print('Tenho o 3')
    print()
else:
    print('Não tenho o 3')
    print()
# Aceita valor duplicado
lista = [99, 2, 35, 23, 2, 34, 12, 1, 44, 5]
print(f'Lista: {lista} com {len(lista)} elementos')
print()

# Aceita valor duplicado
tupla = (99, 2, 35, 23, 2, 34, 12, 1, 44, 5)
print(f'Tupla: {tupla} com {len(tupla)} elementos')
print()

# Não aceita chave duplicada
dicionario = {}.fromkeys([99, 2, 35, 23, 2, 34, 12, 1, 44, 5], 'dict')
print(f'Dicionário: {dicionario} com {len(dicionario)} elementos')
print()

# Não aceita valor duplicado
conjunto = {99, 2, 35, 23, 2, 34, 12, 1, 44, 5}
print(f'Set: {conjunto} com {len(conjunto)} elementos')
print()