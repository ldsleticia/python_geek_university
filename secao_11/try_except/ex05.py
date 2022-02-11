def pega_valor(dicionario, chave):
    try:
        return dicionario[chave]
    except KeyError:
        return None
    except TypeError:
        return None


dic = {"nome": "Geek"}
print(pega_valor(dic, "nome"))

dic2 = {"nome": "Amora"}
print(pega_valor(dic2, "nome"))
