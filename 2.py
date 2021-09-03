valores = []
maior = 0
menor = 0

valores.append(int(input("Digite um valor (Para encerrar o programa digite -1): ")))

for i in valores:
    if i > 0:
        valores.append(int(input("Digite um valor (Para encerrar o programa digite -1): ")))
    if i == 0:
        maior = menor = valores[i]
    else:
        menor = min(valores)
        maior = max(valores)
    if i == -1:
        valores.pop()
        break;
            
print(f'Você digitou os valores {valores}')
print(f'O maior valor digitado foi {maior} na(s) posição(ões)', end='')
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i}...', end='')
print()

print(f'O menor valor digitado foi {menor} na(s) posição(ões) ', end='')
for i, v in enumerate(valores): 
    if v == menor:
        print(f'{i}...', end='')
print()