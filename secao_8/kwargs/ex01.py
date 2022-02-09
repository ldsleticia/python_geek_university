def cores_favoritas(**kwargs):
    for (
        pessoa,
        cor,
    ) in kwargs.items():
        print(f"A cor favorita de {pessoa.title()} é {cor}")


cores_favoritas(marcos="verde", julia="amarelo", fernanda="azul", vanessa="branco")
