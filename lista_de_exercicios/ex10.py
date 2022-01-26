lista = []

while len(lista) < 15:
    notas = int(input('Digite as notas dos alunos: '))
    lista.append(notas)
    
soma = sum(lista)
media = soma / (len(lista))
print(f'A média das notas dos seus 15 alunos é de {media}')