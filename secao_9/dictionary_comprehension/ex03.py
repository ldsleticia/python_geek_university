chaves = "abcde"
valores = [1, 2, 3, 4, 5]

# Nesse caso a chave na posição 0 será o a
# O valor na posição 0 será o 1
# Nesse dictionary comprehension, o que estamos fazendo é passando as letras para que sejam as chaves
# dos números que temos em nossa lista
mistura = {chaves[i]: valores[i] for i in range(0, len(chaves))}
print(mistura)
