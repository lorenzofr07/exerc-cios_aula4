opc = int(input('1- cad \n2-alt \n3-exc \n4-sair'))

match opc:
    case 1:
        print('cadastrar')
    case 2:
        print('alterar')
    case 3:
        print('excluir')
    case 4:
        print('sair')
    case 5:
        print('valor errado')