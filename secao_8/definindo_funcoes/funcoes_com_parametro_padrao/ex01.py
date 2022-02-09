def exponenciacao(
    numero=2, potencia=2
):  # Caso eu informe um valor padrão, a função funciona por default
    return numero**potencia


print(exponenciacao(2, 3))  # 2 * 2 * 2 = 8
print(exponenciacao(3, 2))  # 3 * 3 = 9

print(exponenciacao(3))  # Por padrão eleve ao quadrado
print(exponenciacao(3, 5))  # Eleva a potência informada pelo usuário
