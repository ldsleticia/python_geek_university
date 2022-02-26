class Lampada:
    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade


class ContaCorrente:
    contador = 4999

    def __init__(self, limite, saldo):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        ContaCorrente.contador = self.__numero


class Produto:
    contador = 0

    def desconto(self, porcentagem):
        return (self.__valor * (100 - porcentagem)) / 100

    def __init__(self, nome, descricao, valor):
        self.__id = Produto.contador + 1
        self.__nome = nome
        self.__descricao = descricao
        self.__valor = valor
        Produto.contador = self.__id


class Usuario:
    def __init__(self, nome, sobrenome, email, senha):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = senha

    def nome_completo(self):
        return f"{self.__nome} {self.__sobrenome}"


p1 = Produto("PS4", "Video game", 2300)
print(p1.desconto(20))

user1 = Usuario("Angelina", "Jolie", "angelina@gmail.com", "123456")
user2 = Usuario("Margarete", "Simpson", "margarete@gmail.com", "654321")
print(user1.nome_completo())
print(Usuario.nome_completo(user1))
print(user2.nome_completo())
