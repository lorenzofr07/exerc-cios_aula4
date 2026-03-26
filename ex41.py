def validar(frase):
    return frase != ''

arq = open('dados.txt', 'w', encoding = 'utf-8')

while True:
    frase = input('Digite algo: ')
    if frase.lower() == 'sair':
        break

    if validar(frase) == False:
        print('frase errada')
        continue
    
    arq.write(frase + '\n')

arq.close()