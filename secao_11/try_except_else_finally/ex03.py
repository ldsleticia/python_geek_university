# Forma semi genérica


def divide(a, b):
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError):
        return "Ocorreu um problema"


num1 = input("Informe o primeiro número: ")
num2 = input("Informe o primeiro número: ")

print(divide(num1, num2))
