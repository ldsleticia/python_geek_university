import statistics

valores = 1, 2, 3, 4, 5, 6
media = sum(valores) / len(valores)
print(media)

dados = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]
media = statistics.mean(dados)

# Filtrados todos os dados que são maiores que a média
res = filter(lambda x: x > media, dados)
print(list(res))
