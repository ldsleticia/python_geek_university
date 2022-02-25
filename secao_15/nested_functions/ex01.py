from random import choice


def cumprimento(pessoa):
    def humor():
        return choice(("eai ", "suma daqui ", "gosto muito de você "))

    return humor() + pessoa


print(cumprimento("Amanda"))
print(cumprimento("Julia"))
