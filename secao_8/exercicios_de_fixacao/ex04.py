def quadrado_perfeito(num):
    raizQ = int(num ** (1/2))

    if((raizQ ** 2) == num):
        print(f'O número {num} é um quadrado perfeito!!!'.format(int(num)))
    else:
        print(f'O número {num} não é quadrado perfeito!!!'.format(num))

quadrado_perfeito(2704)
quadrado_perfeito(4598)