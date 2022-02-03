# Função de jogo de moeda
from random import random

def joga_moeda():
    valor = random()
    if valor > 0.5:
        return 'Cara'
    print(valor)
    return 'Coroa'

print(joga_moeda())