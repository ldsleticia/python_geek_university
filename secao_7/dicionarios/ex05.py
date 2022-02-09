"""Carrinho de compras:
Produto 1:
    - nome;
    - quantidade;
    - preço;
Produto 2:
    - nome;
    - quantidade;
    - preço;"""
# Listas

carrinho = []
produto1 = ["PS4", 1, 2300.00]
produto2 = ["GoW 4", 1, 150.00]

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)
print()

# Tuplas

produto1 = ("PS4", 1, 2300.00)
produto2 = ("GoW 4", 1, 150.00)

carrinho = (produto1, produto2)

print(carrinho)
print()

# Dicionários
carrinho = []
produto1 = {"nome": "PS4", "quantidade": 1, "preço": 2300.00}
produto2 = {"nome": "GoW 4", "quantidade": 1, "preço": 150.00}

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)
print()
