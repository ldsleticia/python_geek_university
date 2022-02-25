from random import choice


def faz_me_rir(pessoa):
    def dando_risada():
        risada = choice(("hahaha", "kakaka", "kikiki"))
        return f"{risada} {pessoa}"

    return dando_risada


rindo = faz_me_rir("Fernanda")
print(rindo())
print(rindo())
print(rindo())
