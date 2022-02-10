# Reduce

- A partir do Python v3 e acima, deixou de ser uma função integrada

- Para utilizá-la, necessita de importação a partir do módulo functools

- No lugar do reduce, em 99% dos casos, é mais interessante se usar um ***for***

- Para entender o reduce() imagine que você tem uma coleção de dados e você tem uma função que recebe dois parâmetros. A função reduce() funciona da seguinte forma

~~~
def funcao(x, y):
    return x * y
~~~

- Assim como map() e filter() recebe dois parâmetros sendo uma função o e um iterável:

~~~
reduce(funcao, dado)
~~~

- A funcao reduce() funciona da seguinte forma:
    - Passo 1: res1 = f(a1, a2) # Aplica a função nos dois primeiros elementos da coleção e guarda o resultado
    - Passo 2: res2 = f(res1, a3) # Aplica a função passando o resultado do passo 1 + o terceiro elemento e guarda o res

Isso é repetido até o final, ou seja, em cada passo ela aplica a função passando como primeiro argumento o resultado da aplicação anterior. No final, reduce() retorna o resultado final