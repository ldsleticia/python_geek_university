def cumprimento_especial(**kwargs):
    if 'nome' in kwargs and kwargs['nome'] == 'Letícia':
        return 'Olá Deusa do Egito'
    elif 'nome' in kwargs:
        return f"Oi meu chapa. Seu nome é {kwargs['nome']}"
    return 'Não sei quem é você'

print(cumprimento_especial(nome='Letícia'))
print(cumprimento_especial(nome='Carlos Alberto'))
print(cumprimento_especial())