def eh_positivo(numero):
    if numero == 0:
        return 0
    elif numero % 2 == 0:
        return 1
    else:
        return -1

print(eh_positivo(0))
print(eh_positivo(2))
print(eh_positivo(3))