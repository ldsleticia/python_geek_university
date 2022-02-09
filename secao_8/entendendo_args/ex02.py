def verifica_info(*args):
    if "Letícia" in args:
        return "Bem vinda Letícia"
    return "Não tenho certeza de quem é você..."


print(verifica_info("Letícia"))
print(verifica_info("Gabriel"))
