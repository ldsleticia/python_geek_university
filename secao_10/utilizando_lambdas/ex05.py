autores = [
    "Alyson Noël",
    "John Green",
    "J.K. Rowling",
    "H. G. Wells",
    "Zygmunt Bauman",
    "Friedrich Nietzsche",
    "Edgar Allan Poe",
    "Agatha Christie",
    "Cora Coralina",
]

# Ordenando pelo sobrenome
autores.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower())
print(autores)