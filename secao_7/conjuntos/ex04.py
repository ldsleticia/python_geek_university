# Copiando conjuntos

# Forma 1 - Deep Copy
s = {1, 2, 3}
novo = s.copy()
novo.add(4) # Aqui adiciona um valor

# Forma 2 - Shallow Copy
novo = s
novo.add(4)