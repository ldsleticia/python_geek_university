cidades = [
    ("Berlin", 29),
    ("Cairo", 36),
    ("Buenos Aires", 19),
    ("Los Angeles", 26),
    ("Tokio", 27),
    ("Nova Iorque", 28),
    ("Londres", 22),
]

print(cidades)

# Dado na posição 0 é o nome e o dado na posição 1 é o valor
c_para_f = lambda dado: (dado[0], (9 / 5) * dado[1] + 32)
print(list(map(c_para_f, cidades)))
