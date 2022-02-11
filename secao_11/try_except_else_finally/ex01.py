# Toda a entrada de usuário deve ser tratada
# A função do usuário é destruir o seu sistema
# Finally geralmente é utilizado para fechar ou desalocar recursos como por exemplo desconectar do BD

try:
    num = int(input("Informe um número: "))
    # print(f'Você digitou {num}')
    # Dessa forma, não precisa do else
except ValueError:
    print("Valor incorreto")
except TypeError:
    print("Esse dado não está correto")
else:
    print(f"Você digitou {num}")
finally:
    print(f"Executando o finaly")  # Sempre executado, independente de dar erro ou não
