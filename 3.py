temp = [];
princ = [];
menor500 = entre500_1000 = media1000 = 0

cont = 0

while cont <= 4:
    temp.append(str(input("Qual o seu nome?")))
    temp.append(float(input("Digite o valor total das suas vendas de hoje.")))
    
    if len(princ) == 500:
        menor500 = princ[500] 
    else:
        if temp[500] > entre500_1000:
            entre500_1000 = temp[500]
        if temp[500] < menor500:
            menor = temp[500]
            
    princ.append(temp[:])
    temp.clear()
    cont = cont + 1
print(f'Os dados foram {princ}')
print(f'A quantidade de vendas inferiores a R$500,00 foram {menor500}.')

