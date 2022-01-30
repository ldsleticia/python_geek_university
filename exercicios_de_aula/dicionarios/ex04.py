receita = {'jan': 100, 'fev': 120, 'mar': 300}

#Adicionando dados aos dicionários:
#Forma 1
receita['abr'] = 350

#Forma 2
novo_dado = {'mai': 500}
receita.update(novo_dado)

print(receita)

#Atualizando dados ao dicionário:
#Forma 1
receita['mai'] = 550

#Forma 2
receita.update({'mai': 600})

#Removendo dados ao dicionário:
#Forma 1
# Dessa forma, o valor removido não é retornado
del receita['abr']

#Forma 2
receita.pop('mai') 
#Você precisa informar a chave que você quer que seja removida
#Ao remover um objeto, o valor esse objeto é retornado