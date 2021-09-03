def pesquisa(operacao, *quantidade):
    if operacao == 'media_salario_populacao':
        total_salarios = 0
        salarios = []
        for value in quantidade:
            salarios.append(value)
            total_salarios = total_salarios + value
            media = total_salarios / len(salarios)
        return f'Média salarial da população R$ {media}'

    elif operacao == 'media_numero_filhos':
        total_filhos = 0
        filhos = []
        for value in quantidade:
            filhos.append(value)
            total_filhos = total_filhos + value
            media = total_filhos / len(filhos)
        return f'Média do número de filhos é: {media}'
    
    elif operacao == 'maior_salario':
        salarios = []
        for value in quantidade:
            salarios.append(value)
        return f'O maior salário é de R$ {max(salarios)}'
    
    elif operacao == 'salario_inferior_ao_minimo':
        populacao_total = []
        salarios = []
        for value in quantidade:
            populacao_total.append(value)
            if value < 1100:
                salarios.append(value)

        qtd_populacao = len(populacao_total)
        salario_inferior_minimo = len(salarios)

        percentual = (salario_inferior_minimo * 100) / qtd_populacao
        return(f'Numa população total de {qtd_populacao} pessoas, {salario_inferior_minimo} recebem salário inferior ao salário mínimo. \n'
        f'equivale à {percentual}% da população total')


print(pesquisa('media_salario_populacao', 12, 125.55, 151, 152, 125, 555))
print(pesquisa('media_numero_filhos', 12, 125.55, 151, 152, 125, 555))
print(pesquisa('maior_salario', 12, 125.55, 151, 152, 125, 555))
print(pesquisa('salario_inferior_ao_minimo', 12, 5000.55, 151, 152, 125, 555, 1200))
print(pesquisa('salario_inferior_ao_minimo', 1, 2, 3, 4, 5, 6000, 7000, 8000, 9000, 10000))