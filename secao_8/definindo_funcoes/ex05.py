def nova_funcao1(): # Retorna 4 pois variável é True
    variavel = True
    if variavel:
        return 4
    elif variavel is None:
        return 3.2
    return 'B'

def nova_funcao2(): # Retorna 3.2 pois variável é None
    variavel = None
    if variavel:
        return 4
    elif variavel is None:
        return 3.2
    return 'B'

def nova_funcao3(): # Retorna 'B' pois variável é False
    variavel = False
    if variavel:
        return 4
    elif variavel is None:
        return 3.2
    return 'B'

print(nova_funcao1())
print(nova_funcao2())
print(nova_funcao3())