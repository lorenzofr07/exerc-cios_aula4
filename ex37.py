def faixa_etaria(idade):
    if idade <= 0:
        return 'Idade inválida'
    if idade < 12:
        return 'criança'
    elif idade < 17:
        return 'Adolescente'
    else:
        return 'Adulto'

while True:
    idade = input('Digite a idade ou SAIR: ')
    if idade.lower() == 'sair':
        break
    print(faixa_etaria(int(idade)))

print('Até mais...')