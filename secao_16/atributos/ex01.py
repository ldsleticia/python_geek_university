class Produto:
    imposto = 1.05
    contador = 0

    def __init__(self, nome, descricao, valor):
        self.id = Produto.contador + 1
        self.nome = nome
        self.descricao = descricao
        self.valor = valor * Produto.imposto
        Produto.contador = self.id


p1 = Produto("PS4", "Video game", 2300)
p2 = Produto("XboxS", "Video game", 4500)
p3 = Produto("arroz", "mercearia", 5.99)
p3.peso = "5kg"

print(p3.peso)
print(p1.__dict__)
print(p2.__dict__)
print(p3.__dict__)

del p3.peso

