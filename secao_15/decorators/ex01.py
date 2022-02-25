# Sintaxe não recomendada

def seja_educado(funcao):
    def sendo():
        print("Foi um prazer conhecer você")
        funcao()
        print("Tenha um ótimo dia")

    return sendo


def saudacao():
    print("Seja bem vindo, seja bem vinda a Geek University")


teste = seja_educado(saudacao)
teste()
