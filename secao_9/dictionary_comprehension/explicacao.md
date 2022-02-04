# Dictionary Comprehension

Pense no seguinte:

Se quisermos criar uma lista fazemos:

~~~
lista = [1, 2, 3, 4]
~~~

Se quisermos criar uma tupla fazemos:

~~~
tupla = 1, 2, 3, 4
~~~

Se quisermos criar um dicionário fazemos:

~~~
dicionario = dict(a=1, b=2, c=3, d=4)
~~~

Se quisermos criar um set fazemos:

~~~
conjunto = {1, 2, 3, 4}
~~~

- A sintaxe do dictionary comprehension é:

~~~
{chave: valor for valor in iteravel}
~~~

Um exemplo segue abaixo:

~~~
numeros = dict(a=1, b=2, c=3, d=4, e=5)
quadrado = {chave: valor ** 2 for chave, valor in numeros.items()}
~~~

No caso acima, o .itens() nos é retornado uma lista de tuplas e para cada chave e valor dentro dessas tuplas, 
o programa coloca a chave dentro de chave e eleva o valor ao quadrado