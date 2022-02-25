# Decoradores ou Decorators

- São funções e assim como qualquer função, são de primeira classe

- Envolvem outras funções e aprimoram seus comportamentos

- Também são exemplos de HOF

- Tem uma sintaxe própria, usando o ***@*** (Syntact sugar)

- Geralmente uma função decorator recebe como parametro uma funcao
~~~
/---------------------------------/
/        Function Decotator       /
-----------------------------------

------------------------------------

/ /---------------------------------/ /
/ /        Function Decotator       / /
/ /---------------------------------/ /
~~~

- Decoradores podem ter diferentes assinaturas, ou seja, conter diferentes
assinaturas de entrada

- Quando nossa funçãoq ue será a decorator recebe menos parâmetros que as funções
decoradas, teremos um TypeError e para resolver isso, precisamos usar o 
***Decorator Pattern***

- Vale lembrar que podemos usar parâmetros nomeados. Ex:
~~~
def ordenar(principal, acompanhamento):
    return f'Eu gostaria de {principal}, acompanhado de {acompanhamento}, por favor'
    
print(ordenar(acompanhamento='Batata frita', principal='Picanha'))
~~~