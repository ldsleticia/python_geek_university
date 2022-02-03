def data_por_extenso(dia, mes, ano):
    meses = 'janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro'
    print ('A data que você colocou é :')
    print ('%s de %s de %s' %(dia, meses[int(mes) - 1], ano))

data_por_extenso(12, 12, 2012)