arquivo = open(
    "/home/leticia/Documentos/python_geek_university/secao_13/leitura_de_arquivos/texto.txt"
)

print(arquivo.read())
arquivo.seek(0)  # Voltou para a posição 0 do arquivo
print(arquivo.read())
arquivo.seek(22)  # Voltou para a posição 22 do arquivo
print(arquivo.read())
