#verifique se a nota é válida
nota = int(input("Digite sua nota: "))
while nota < 0 or nota > 10:
    print("Digite uma nota válida entre 0 e 10: ")
    nota = int(input("Digite nota válida: "))
print("Sua nota é válida")

#somatório de N números inteiros á partir do primeiro.
contador = 1
acumulador = 0
numero = int(input("\n Digite seu número inteiro: "))
while contador <= numero:
    acumulador = acumulador + contador
    contador = contador + 1
print("Resultado: ", acumulador)

#quando for -1 dar a media e encerrar
numero = int(input("Digite seus numeros para obter a media, para obter o resultado digite (-1): "))
contador = 0
quantidade = 0
while numero != -1:
    contador = contador + numero
    quantidade = quantidade + 1
    numero = int(input("Digite números (-1 para parar): "))
media = contador / quantidade
print("Média:", media)

#receber 10 numeros e ver e é par ou impar

pares = 0
impar = 0
contador = 0
while contador < 10:
    numero = int(input("Digite seu numero aqui: "))
    if numero % 2 == 0:
        pares = pares + 1
    else:
        impar = impar + 1

    contador = contador + 1
print("Quantidade de pares ", pares)
print("Quantidade de impares ", impar)

#calculadora simples
while True:
    print("\n CALCULADORA")
    print("1: SOMA")
    print("2: SUBTRAÇÂO")
    print("3: MULTIPLICAÇÂO")
    print("4: DIVISÂO")
    print("0: SAIR")
    opcao = int(input(" Escolha uma opção: "))
    if opcao == 0:
        print(" SAINDO ")
        break
    elif opcao >= 1 and opcao <= 4:
        n1 = float(input("Digite o primeiro número: "))
        n2 = float(input("Digite o segundo número: "))
        if opcao == 1:
            print("Resultado: ", n1 + n2 )
        elif opcao == 2:
            print("Resultado: ", n1 - n2)
        elif opcao == 3:
            print("Resultado: ", n1 * n2)
        elif opcao == 4:
            if n2 == 0:
                print("Não é possivel dividir por 0")
            else:
                print("Resultado: ", n1 / n2)
    else:
        print("Opçao invalida")

