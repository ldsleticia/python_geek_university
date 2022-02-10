# All e Any

- all() é uma função booleana e retorna True se ***todos*** os elementos do iterável são o verdadeiros ou se o iterável está vazio. Exemplo:

~~~
print(all([0, 1, 2, 3, 4])) # -> False
print(all([])) # -> True

nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina',]
print(all([nome[0] == 'C' for nome in nomes])) # -> True

nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina', 'Vanessa']
print(all([nome[0] == 'C' for nome in nomes])) # -> False
~~~

- any() retorna True se ***qualquer*** elemento do iterável for verdadeiro. Se o iterável estiver vazio, retorna false

~~~
print(all([0, 1, 2, 3, 4])) # -> True
print(all([])) # -> False

nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina', 'Vanessa']
print(all([nome[0] == 'C' for nome in nomes])) # -> True
~~~