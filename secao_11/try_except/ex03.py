# Tratando um erro específico e usando um alias para o erro

try:
    len(5)
except TypeError as err:
    print(f"A aplicação gerou o seguinte erro: {err}")
