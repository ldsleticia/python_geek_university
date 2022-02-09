def nome_completo(nome, sobrenome):
    return f"Seu nome completo é {nome} {sobrenome}"


nome = "Elijah"
sobrenome = "S"

# KeyWord arguments
print(nome_completo(nome="Letícia", sobrenome="S"))
print(nome_completo(nome=nome, sobrenome=sobrenome))
print(nome_completo(sobrenome="S", nome="Letícia"))
