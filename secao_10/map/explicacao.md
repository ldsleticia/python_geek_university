# MAP

- Com o Map fazemos mapeamento de valores para função

- Map é uma função que recebe dois parâmetros, o primeiro é a função e o segundo um iterável. Exemplo:

~~~
# Função 
def area(r):
    return math.pi * (r * 2)

# Iterável
raios = [2, 5, 7.1, 0.3, 10, 44]

areas = map(area, raios)
~~~

- Após utilizar a função Map e usar seu resultado, ele será zerado