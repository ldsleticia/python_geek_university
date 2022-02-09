from functools import total_ordering


def soma_numeros(*args):
    return sum(args)


def multiplica_numeros(*args):
    total = 1
    for numero in args:
        total *= numero
    return total


print(soma_numeros(2, 3, 4, 5))
print(multiplica_numeros(2, 3, 4, 5))
