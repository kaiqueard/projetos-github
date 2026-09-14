#crescente
numero = 1
while numero <= 10:
    print(numero)
    numero += 1

#decrescente
numero2 = 10
while numero2 > 0:
    print(numero2)
    numero2 -= 1

#solicitar um valor e imprimir a tabuada
numero3 = 1
valor = int(input("\n Digite um valor de 1 a 10 para receber sua tabuada: "))
while valor <= 0 or valor > 10:
    print("invalido, coloque um numero entre 1-10")
    valor = int(input(" Valor valido: "))
while numero3 <= 10:
    print(numero3 * valor)
    numero3 += 1

#a palavra minimo 3 e maximo 10
palavra = input("Digite sua palavra: ")
#se invalido
while len(palavra) < 3 or len(palavra) > 10:
    print("Palavra inválida, maiorr que 10 ou menor que 3")
    palavra = input("palavra: ")
print(palavra, len(palavra))