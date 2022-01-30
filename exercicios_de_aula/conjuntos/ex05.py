# Gerar conjuntos únicos

estudantes_python = {'Marcos', 'Patricia', 'Ellen', 'Pedro', 'Julia', 'Guilherme'}
estudantes_java = {'Fernando', 'Gustavo', 'Julia', 'Ana', 'Patricia'}

# Forma 1 - Utilizando Union
unicos = estudantes_python.union(estudantes_java)
print(unicos)
print()

# Forma 2 - Utilizando o caractere pipe (|)
unicos2 = estudantes_python | estudantes_java
print(unicos2)
print()

#Gerar conjunto de estudantes que estão em ambos os conjuntos

# Forma 1 - Utilizando intersection
ambos1 = estudantes_python.intersection(estudantes_java)
print(ambos1)
print()

# Forma 2 - Utilizando intersection &
ambos2 = estudantes_python & estudantes_java
print(ambos2)
print()

#Gerar conjunto de estudantes que estão em um curso mas não no outro

so_python = estudantes_python.difference(estudantes_java)
print(so_python)
print()

so_java = estudantes_java.difference(estudantes_python)
print(so_java)
print()