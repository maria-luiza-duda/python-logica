alturaTotal = float(0);
mediaAlturas = float(0);
idade = int(1);
soma = 0;

idade = int(input("Qual a idade?"))
altura = float(input("Qual a altura?"))

while idade > 0 :
    
    idade = int(input("Qual a idade?"))
    altura = float(input("Qual a altura?"))

    if idade <= 0:
        break;

    if idade > 50:
        soma = soma + 1;
        alturaTotal = alturaTotal + altura;

mediaAlturas = alturaTotal / soma;
print("A media de altura das pessoas com mais de 50 anos é: {}".format(mediaAlturas));