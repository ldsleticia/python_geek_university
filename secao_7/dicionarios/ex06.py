# Copiando dicionários
# Forma 1 - Deep Copy
d = dict(a=1, b=2, c=3)

novo = d.copy
novo["d"] = 4

# Forma 2 - Shallow Copy (ambos serão alterados, o original e o que recebeu a cópia)
novo = d
novo["d"] = 4
