# Removendo elementos do set
# Forma 1
s = {1, 2, 3}
s.remove(3) #não é indice, é valor. Caso não encontre, retorna KeyError
print(s)

s.discard(2) #Caso não encontre, não retorna nenhum erro
print(s)