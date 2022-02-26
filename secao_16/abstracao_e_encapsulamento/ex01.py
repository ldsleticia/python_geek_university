class Conta:

    contador = 400

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    def extrato(self):
        print(
            f"Saldo de {self.__saldo} do titular {self.__titular} com limite de {self.__limite}"
        )

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
        else:
            print("O valor precisa ser positivo")

    def sacar(self, valor):
        if valor > 0:
            if self.__saldo >= valor:
                self.__saldo -= valor
            else:
                print("Saldo insuficiente")
        else:
            print("O valor deve ser positivo")

    def transferir(self, valor, conta_destino):
        self.__saldo -= valor
        self.__saldo -= 10
        conta_destino.__saldo += valor


conta1 = Conta("Angelina", 150.00, 1500.00)
conta1.extrato()

conta2 = Conta("Julia", 300.00, 2000.00)
conta2.extrato()

conta1.transferir(100, conta2)
conta1.extrato()
conta2.extrato()
