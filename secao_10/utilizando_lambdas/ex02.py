# O strip() retira os espaços que a string pode conter no início e no fim da variável
# Não retira os espaços entre as palavras
nome_completo = lambda nome, sobrenome: nome.strip().title() + sobrenome.strip().title()
