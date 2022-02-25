def gritar(funcao):
    def aumentar(*args, **kwargs):
        return funcao(*args, **kwargs).upper()

    return aumentar


@gritar
def saudacao(nome):
    return f"Olá eu sou o/a {nome}"


@gritar
def ordenar(principal, acompanhamento):
    return f"Eu gostaria de {principal}, acompanhado de {acompanhamento}, por favor"


print(saudacao("Angélica"))
print(ordenar("Picanha", "batata frita"))
