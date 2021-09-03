nome = input("Digite o nome do arquivo que você quer ler: ")
def abrir_arquivo (nome):
    arquivo = open (nome, "r")
    for i in arquivo.readlines():
        print(i)
    arquivo.close()
abrir_arquivo(nome)

novo_arq= input("Digite o nome do arquivo que você quer criar: ")
def criar_arquivo (novo_arq):
    arquivo = open(novo_arq, "wt+")
    arquivo.write("Maria 8 \n")
    arquivo.write("Luiza 7.8 \n")
    arquivo.write("Duda 7.25 \n")
    arquivo.close()
    print(f'Arquivo {novo_arq} foi criado.')
criar_arquivo(novo_arq)
