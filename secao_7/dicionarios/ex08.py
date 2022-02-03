#Iterando dicionários

receita = {'jan': 100, 'fev': 250, 'mar': 400}

for chave in receita:
    print(chave)
print()

for chave in receita:
    print(receita[chave])
print()

for chave in receita:
    print(f'{chave} : recebi {receita[chave]}')
print()

print(receita.keys())
print()

#Acessando os valores
print(receita.values())
print()

for valor in receita.values():
    print(valor)
print()

#Desempacotar dicionários
for chave, valor in receita.items():
    print(f'chave={chave} e valor={valor}')
print()

print(sum(receita.values()))
print(max(receita.values()))
print(min(receita.values()))
print(len(receita))