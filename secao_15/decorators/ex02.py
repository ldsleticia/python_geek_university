# Sintaxe recomendada


def seja_educado_mesmo(funcao):
    def sendo_mesmo():
        print("Foi um prazer conhecer você")
        funcao()
        print("Tenha um ótimo dia")

    return sendo_mesmo


@seja_educado_mesmo
def apresentando():
    print("Meu nome é Pedro")


apresentando()
