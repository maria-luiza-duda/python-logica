lista_de_vendas = []
a_inferior_500 = []
b_entre_500_1000 = []
c_acima_1000 = []

for i in range(2):
    nome = input(f'Informe o nome do(a) vendedor(a) {i+1}: ')
    venda = float(input(f'A quantidade de vendas do(a) vendedor(a) {nome} em R$ foi de: '))
    if venda < 500:
        a_inferior_500.append([nome.title(), venda])

    elif (venda > 500) and (venda < 1000):
        # nome dos vendedores
        b_entre_500_1000.append(nome.title())
    elif venda > 1000:
        # valores das vendas
        c_acima_1000.append(venda)

    print()
    print('-' * 30)
    print()

qtd_vendas_inferiores_500 = len(a_inferior_500)

soma_vendas_acima_1000 = 0
for venda in c_acima_1000:
    soma_vendas_acima_1000 += venda

media_vendas_acima_1000 = soma_vendas_acima_1000 / len(c_acima_1000)


print(f'a. Quantidade de vendas inferiores a R$ 500,00: {qtd_vendas_inferiores_500}')
print(f'b. Nome dos vendedores que realizaram vendas entre R$500,00 e R$ 1000,00: {b_entre_500_1000}')
print(f'c. Média das vendas acima de R$1000,00: {media_vendas_acima_1000}')