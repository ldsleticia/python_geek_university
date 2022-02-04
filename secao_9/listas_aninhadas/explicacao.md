# Listas Aninhadas

- Algumas linguagens de programação possuem uma estrutura de dados chamada de arrays:
    - Podem ser unidimensionais ou Arrays/Vetores -> [ ]
    - Multidimensionais ou Matrizes -> [ [ ] ] 
<br>
<br>
- Em Python, esses arrays se chamam listas que como já vimos, aceitam qualquer tipo de dados e não 
tem um tamanho fixo como em outras linguagens

- Listas aninhadas são o correspondente às matrizes em outras linguagens

Um exemplo segue abaixo:

~~~
listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
~~~

A lista acima, é uma lista de tamanho 3 x 3ou seja, contém três linhas e três colunas sendo:

    - Cada lista uma linha 

    - Cada item da lista, uma coluna

- Para acessar os dados, você precisa colocar o índice da lista e o índice do item que você quer acessar da lista

Um exemplo segue abaixo:

~~~
print(listas[0][1])
~~~

Usando o exemplo acima, você acessa o segundo item da primeira lista, no caso do exemplo, a lista [1, 2, 3] e
o número 2