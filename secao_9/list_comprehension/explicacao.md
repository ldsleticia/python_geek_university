# List Comprehension

- Utilizando List Comprehension nós podemos gerar novas listas com dados processados a partir de outro iteravel

- Sua sintaxe começa com colchetes e se dá da seguinte forma:

~~~
[dado for dado in iteravel]
~~~

Um exemplo abaixo:

~~~
numeros = [1, 2, 3, 4, 5]
res = [numero * 10 for numero in numeros]
print(res)
~~~

A expressão acima pode ser dividida em duas partes, sendo a primeira:

~~~
for numero in numeros
~~~

E a segunda parte:

~~~
numero * 10
~~~