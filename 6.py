nota1 = int(input("Qual o valor da sua primeira nota?"))
nota2 = int(input("Qual o valor da sua segunda nota?"))
letra = str(input("Qual média voce quer saber primeiro? Digite A para aritmética, P para ponderada e S para fechar o programa."))


def media (nota1, nota2, letra):
    
    while letra == "A" or letra == "P":
        
        if letra == "A":
            mediaA = (nota1 + nota2) / 2
            print("A média aritmética foi ", mediaA)
            
        elif letra == "P":
            mediaP = ((nota1 * 8) + (nota2 * 2)) / 10
            print("A média ponderada foi ", mediaP)
        
        letra = str(input("Digite a letra restante."));

media(nota1, nota2, letra);