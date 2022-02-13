# Builtin

- São módulos integrados, ou seja, já vem instalados no python

- É necessário realizar o import dessas funções pois o Python não faz o carregamento automático para poupar memória

- É possível se utilizar alias (apelidos) para as funções Builtin e ficaria da seguinte forma:

~~~
import random as rdm

print(rdm.random())
~~~

- Podemos importar todas as funções de um módulo usando o nome da função e o *. Exemplo:

~~~
from random import *
~~~

- Podemos também das alias a funcoes. Exemplo:

~~~
from random import randint as rdi

print(random.rdi(5, 89))
~~~