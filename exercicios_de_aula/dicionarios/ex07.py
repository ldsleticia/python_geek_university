# Forma não usual de criação de dicionários
# Forma 1

outro = {}.fromkeys('a', 'b')
print(outro)
print()
usuario = {}.fromkeys(['nome', 'pontos', 'email', 'profile'], 'desconhecido')
print(usuario)
print()
veja = {}.fromkeys('teste', 'valor')
print(veja)
print()
veja = {}.fromkeys(range(1,11), 'novo')
print(veja)
print()
# O método fromkeys recebe dois parâmetros: um iterável e um valor
# Para cada valor do iterável, ele atribuirá um valor a essa chave