# F = C * (9.0/5.0) + 32
def converte_temperatura(graus):
    f = (graus - 32) * 5/9
    return f

print(converte_temperatura(42))