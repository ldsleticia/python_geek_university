# Primeira forma
pais = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}

# Segunda forma
paises = dict(br='Brasil', eua='Estados Unidos', py='Paraguai')

# Acessar os indices do dicinário
# Primeira forma
print(paises['br'])
print(paises['py'])

# Segunda forma
#pais = (paises.get('br'))

pais = (paises.get('ru', 'Não encontrado')) #Define o que você quer que seja o retorno ao não encontrar o que você procura
print(pais)

print('br'in paises) #True
print('ru' in paises) #False
print('Estdos Unidos') #False, não procura por valor, somente por chave

if 'ru' in paises:
    russia = paises['ru']

#if pais:
#    print(f'Encontrei o país {pais}')
#else:
#   print(f'Não encontrado')