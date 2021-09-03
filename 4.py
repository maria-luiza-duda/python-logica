soma = 0
num1 = int(input("Digite um valor: "))
num2 = int(input("Digite um valor: "))

def impares_entre(num1, num2):
    global soma
    for c in range(num1, num2 + 1):
        if c % 2 != 0:
            soma = soma + c
    
    print("A soma de todos os valores solicitados é {}".format(soma))

impares_entre(num1, num2)