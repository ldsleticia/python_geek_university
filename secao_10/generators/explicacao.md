# Generators

Veja o código abaixo:

~~~
nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina', 'Vanessa']
print(all([nome[0] == 'C' for nome in nomes]))
~~~

Esse mesmo código poderia ter sido escrito da seguinte forma:

~~~
print(any(nome[0] == 'C' for nome in nomes))
~~~

Essa forma, é o ***generator***. Generator não retorna uma tupla e apartir do momento que você utiliza o dado, o resultado é apagado da memória