nota = float(input('Nota: '))
freq = float(input('Freq: '))

if freq < 75:
    print('Reprovado por falta')

elif nota >= 7:
    print('aprovado')
elif nota >= 75:
    print('AF')
else:
    print('DP')