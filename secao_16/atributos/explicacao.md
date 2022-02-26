# Atributos

- Representam as caracteristicas do objeto. Ou seja, pelos atributos nós conseguimos 
representar computacionalmente os estados de um objeto

- Em Python, dividimos os atributos em três grupos:
  - Atributos de instância;
  - Atributos de clase;
  - Atributos dinâmicos
  
***Atributos de instância*** são declarados dentro do método construtor
~~~
class Lampada:
    def __init__(self, voltagem, cor):
        self.__voltagem = voltagem
        self.__cor = cor
        self.__ligada = False
        
    @property
    def voltagem(self)
        return self.__voltagem
        
    @property
    def cor(self)
        return self.__cor
        
    @property
    def ligada(self)
        return self.__ligada
~~~

- Em Python, ficou estabelecido que todo atributo de uma classe é público.
Caso tenhamos a necessidade do atributo ser privado, utilizamos o duplo underscore
Isso é chamado de name mangling (__)

***Atributos de classe*** são atributos que são declarados diretamente na classe,
ou seja, fora do construtor. Geralmente já inicializamos um valor e este valor
é compartilhado entre todas as instâncias da classe. Ou seja, ao invés de cada
instância da classe ter seus próprios valores como é o caso dos atributos de 
instância, com os atributos de classe, todas as instâncias terão o mesmo valor
para esse atributo
~~~
class Produto():
    imposto = 1.05
    contador = 0
    
    def __init__(self, nome, descricao, valor):
        self.id = Produto.contador + 1
        self.nome = nome
        self.descricao = descricao
        self.valor = (valor * Produto.imposto)
        Produto.contador = self.id
p1 = Produto('PS4', 'Video game', 2300)
p2 = Produto('XboxS', 'Video game', 4500)
~~~

***Atributos dinâmicos*** é um atributo de instância que pode ser 
criado em tempo de execução. Será exclusivo da instância que o criou. É possível
criar e deletar objetos atributos em tempo de execução
~~~
p1 = Produto('PS4', 'Video game', 2300)
p2 = Produto('arroz', 'mercearia', 5.99)
p2.peso = '5kg'
~~~