# Iterators e Iterables

- Iterator ->
  - Um objeto que pode ser iterado.
  - Retorna um dado, sendo um elemento por vez quando uma função next() é chamada
  - Ex: 
  ~~~ 
  nome 'geek'
  numeros = [1, 2, 3, 4, 5, 6]
  ~~~

- Iterable ->
  - Um objeto que irá retornar um iterator quando a função iter() for chamada
  - Para que ox exemplos acima se tornassem iterables, seria necessário colocá=los dentro de uma função iter()
  - Ex:
  ~~~
  iter1 = iter(nome)
  iter2 = iter(numeros)
  ~~~