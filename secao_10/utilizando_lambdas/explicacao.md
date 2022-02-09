# LAMBDA

- São funções sem nome, anônimas

- Precisa se iniciar com a palavra reservada ***lambda***

- É representada da seguinte forma:

~~~
lambda x: 3 * x + 1
~~~

Sem o uso da função lamba, a expressão acima ficaria da seguinte forma:

~~~
def soma(x):
    return 3 + x + 1
~~~

- Para que ela seja chamada, precisamos atribuí-la à uma variável seguindo o exemplo:

~~~
calc = lambda x: 3 * x + 1
print(calc(4))
~~~

- Podem receber multiplas entradas

