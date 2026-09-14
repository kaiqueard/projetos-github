#Ver se está quente ou normal
temperatura = float(input( "Digite a temperatura: "))
if temperatura >= 25:
    print("quente demais")
elif temperatura <= 10:
    print("frio do carai")
else:
    print('legal')


#Ver se numero inteiro é par
numero = int(input("\n Digite seu numero: "))
if numero % 2 == 0:
    print("é par")
else:
    print("Não é par")


#Sua idade (Maior/Menor)
idade = int(input("\n Digite sua idade: "))
if idade >= 18:
    print("Você é de maior")
else:
    print("Você é de menor betinha")


#Média
media = float(input("\n Digite sua média: "))
if media < 4:
    print("Reprovado")
elif media >= 4 and media < 7:
    print("recuperaçao")
else:
    print("Aprovado")\

#Entrada do cinema filme de terror

idade = int(input("\nDigite sua idade: "))
ingresso = input("Você tem um ingresso?(s/n)").lower()
#transformar em booleano (bool) [verdadeiro ou falso] {letra inicial maiuscula}
if ingresso == "s":
    ingresso = True
elif ingresso == "n":
    ingresso == False
if idade >= 18:
    if ingresso == True:
        print("Bom filme")
    else:
        print("não tem ingresso")
else:
    print("não tem idade")