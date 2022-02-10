usuarios = [
    {"username": "samuel", "tweets": ["Adoro bolo", "Adoro pizza"]},
    {"username": "carla", "tweets": ["Adoro bolo", "Adoro pizza"]},
    {"username": "jeff", "tweets": []},
    {"username": "bob123", "tweets": []},
    {"username": "doggo", "tweets": ["Adoro cachorros", "Vou sair hoje"]},
    {"username": "gal", "tweets": []},
]

# Ordena pela quantidade de chaves
ordena = sorted(usuarios, key=len)

# Ordena pelo username
ordena_username = sorted(usuarios, key=lambda usuario: usuario["username"])

# Ordena pela quantidade de tweets
ordena_tweets = sorted(usuarios, key=lambda usuario: len(usuario["tweets"]))

print(ordena)
print()
print(ordena_username)
print()
print(ordena_tweets)
