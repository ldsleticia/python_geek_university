# Desempacotar com **kwargs


def mostra_nomes(**kwargs):
    return f"{kwargs['nome']} {kwargs['sobrenome']}"


nomes = {"nome": "Letícia", "sobrenome": "Dos Santos"}

print(mostra_nomes(**nomes))
