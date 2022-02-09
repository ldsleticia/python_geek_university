def minha_funcao(idade, nome, *args, solteiro=False, **kwargs):
    print(f"{nome} tem {idade}")
    print(args)
    if solteiro:
        print("Solteiro")
    else:
        print("Em relacionamento")
    print(kwargs)


minha_funcao(8, "Julia")
minha_funcao(18, "Felicity", 4, 5, 3, solteiro=True)
minha_funcao(34, "Felipe", eu="não", voce="vai")
minha_funcao(19, "Carla", 9, 4, 3, java=False, python=True)
