def forca_tipos(*tipos):
    def decorador(funcao):
        def converte(*args, **kwargs):
            novo_args = []
            for (valor, tipo) in zip(args, tipos):
                novo_args.append(tipo(valor))
            return funcao(*args, **kwargs)

        return converte

    return decorador


@forca_tipos(str, int)
def repete_mensagem(msg, vezes):
    for vez in range(int(vezes)):
        print(msg)


repete_mensagem("geek", 3)
