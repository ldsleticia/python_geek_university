# Vários tratamentos de uma só vez

try:
    # len(5)
    geek()
except NameError as errA:
    print(f"A aplicação gerou o seguinte erro: {errA}")
except TypeError as errB:
    print(f"A aplicação gerou o seguinte erro: {errB}")
except:
    print("Erro desconhecido")
