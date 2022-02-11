def divide(a, b):
    try:
        return int(a) / int(b)
    except ValueError:
        return "Valor incorreto"
    except ZeroDivisionError:
        return "Divisao por 0 não é possível"


num1 = input("Informe o primeiro número: ")
num2 = input("Informe o primeiro número: ")

print(divide(num1, num2))
