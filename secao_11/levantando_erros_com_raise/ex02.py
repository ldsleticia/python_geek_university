def colore(texto, cor):
    cores = "verde", "amarelo", "azul", "branco"
    if type(texto) is not str:
        raise TypeError("texto precisa ser uma string")
    if type((cor)) is not str:
        raise TypeError("cor precisa ser uma string")
    if cor not in cores:
        raise ValueError(f"é possivel escolher somente uma das cores {cores}")
    print(f"O texto {texto} será impresso na cor {cor}")


colore("joaozinho", "azul")
colore("joaozinho", 4)
