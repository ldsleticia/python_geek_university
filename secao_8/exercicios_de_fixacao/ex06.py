def converte_em_segundos(horas, minutos, segundos):
    horas_convertidas = horas * 3600
    minutos_convertidos = minutos * 60
    segundos_totais = horas_convertidas + minutos_convertidos + segundos
    return (f'O total de segundos das horas que você passou é de {segundos_totais}')

print(converte_em_segundos(2, 3, 12))