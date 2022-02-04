numeros = [1, 2, 3, 4, 5]

# Aqui ele está dizendo que cada número da lista se tornou uma chave e cada chave recebe 
# O valor ímparou par a depender do resto da divisão daquele número. 
# O 1 virou a chave e ímpar ou par virou o valor. 
# O programa sabe se é ímpar ou par porque ele pega o número, faz a divisão por 2 e verifica se o resultado é 0. 
# Ou seja, o valor foi atribuído a chave mas também foi usado para saber se ele é ímpar ou par
res = {arroz: ('par' if arroz % 2 == 0 else 'impar') for arroz in numeros}
print(res)