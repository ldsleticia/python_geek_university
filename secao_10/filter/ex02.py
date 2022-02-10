usuarios = [
    {"username": "samuel", "tweets": ["Adoro bolo", "Adoro pizza"]},
    {"username": "carla", "tweets": ["Adoro bolo", "Adoro pizza"]},
    {"username": "jeff", "tweets": []},
    {"username": "bob123", "tweets": []},
    {"username": "doggo", "tweets": ["Adoro cachorros", "Vou sair hoje"]},
    {"username": "gal", "tweets": []},
]

# Forma 1
inativos = list(filter(lambda u: len(u["tweets"]) == 0, usuarios))
print(inativos)

# Forma 2
inativos = list(filter(lambda u: not u["tweets"], usuarios))
print(inativos)
