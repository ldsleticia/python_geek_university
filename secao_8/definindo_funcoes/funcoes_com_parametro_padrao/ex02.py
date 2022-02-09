def mostra_informacao(nome="Geek", instrutor="False"):
    if nome == "Geek" and instrutor:
        return "Bem vindo instrutor Geek"
    elif nome == "Geek":
        return "Pensei que você era instrutor"
    return f"Olá {nome}"


print(mostra_informacao())
print(mostra_informacao(instrutor=False))
print(mostra_informacao("Letícia"))
