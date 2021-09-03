num = int(input("Digite um valor: "))
cont = num

def fatorialduplo(num, cont):
    fatorial = 1
    print('Calculando {}! duplo = '.format(num), end='')
    while cont > 0:
        print('{}'. format(cont), end='')  
        print('x' if cont > 1 else ' = ', end='')
        fatorial *= cont
        cont -= 2   
    print('{}'.format(fatorial))

fatorialduplo(num, cont) 