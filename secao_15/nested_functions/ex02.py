from random import choice


def faz_me_rir():
    def rir():
        return choice(("hahaha", "kakaka", "kikikikiki"))

    # Nesse caso ele retorna a função em si e não a execução dela
    return rir


rindo = faz_me_rir()
# Necessário ser impresso dessa forma porque na função trazemos a função rir
# não a execução da função rir. Sem os () apenas mostra o nome do espaço
# de memória onde está alocada aquela variável
print(rindo())
