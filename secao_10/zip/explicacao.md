# ZIP

- Cria um iterável (zip object) que agrega elemento de cada um dos iteráveis passados como entrada em pares

Exemplos:

~~~
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

zip1 = zip(lista1, lista2)
print(zip1)
~~~

- É possível gerar uma lista, uma tupla ou um dicionário com o Zip

- Pega cada um dos elementos e forma tuplas, no exemplo acima, seriam três tuplas e seriam as seguintes:

~~~
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

zip1 = zip(lista1, lista2)
print(zip1)

[(1, 4), (2, 5), (3, 6)]
~~~

- Ao converter um dado zip para tupla, set ou dicionário, após seu primeiro uso, os dados são zerados

- O zip utiliza como parámetro o menor tamanho em iterável, isso significa que se estiver trabalhando com iteráveis de tamanhos diferentes, irá parar quando os elementos do menor iterável acabarem

- Podemos utilizar diferentes iteráveis com zip