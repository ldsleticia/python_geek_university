# Use tuplas sempre que não for mudar os dados da coleção

# Meses por exemplo, são uma lista que não devem ser modificadas
meses = (
    "janeiro",
    "fevereiro",
    "março",
    "abril",
    "maio",
    "junho",
    "julho",
    "agosto",
    "setembro",
    "outubro",
    "novembro",
    "dezembro",
)

#
i = 0
while i < len(meses):
    print(meses[i])
    i = i + 1

for i in meses:
    print(i)

# Se houverem dois iguais, ele retornará a primeira incidência
print(meses.index("julho"))

# Dessa forma, verifica a partir de um ponto específico na tupla (e na lista)
print(meses.index("julho", 6))

# começando do início até o final
print(meses[0:])

# começa do 5 e vai até o número indicado
print(meses[5:9])
