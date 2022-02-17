with open(
    "/home/leticia/Documentos/python_geek_university/secao_13/escrevendo_em_arquivos/frutas.txt",
    "w",
) as arquivo:
    while True:
        fruta = input("Digite o nome de uma fruta ou digite sair ")
        if fruta != "sair":
            arquivo.write(fruta + "\n")
        else:
            break
