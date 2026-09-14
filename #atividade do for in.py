#atividade do for in

#percorra 1 até 100 e mostrar aqueles que sao multiplos de 3 e que nao sao multiplos de 5, no final mostrar quantos numeros atenderam a condição

for i in range(1, 101):
    if i % 3 == 0 and i % 5 != 0:
        print(i)

#numero inteiro positivo, nao continuar se for valido, depois some todos de 1 até o numero, ao final exiva a expressao aritmetica com o resultado

n1 = int(input("Digite um numero inteiro: "))

while n1 <= 0:
    n1 = int(input("Valor invalido digite um número positivo: "))

soma = 0
expressao = ""

for i in range(1, n1 + 1):
    soma = soma + i
    
    if i == n1:
        expressao = expressao + str(i)
    else:
        expressao = expressao + str(i) + " + "

print(expressao, "=", soma)

#peça um numero inicial e um final exiba a tabuada dele de 1 até 10 
inicio = int(input("Digite o número inicial: "))
fim = int(input("Digite o número final: "))

for i in range(inicio, fim + 1):
    print(f"Tabuada do {i}:")
    
    for i2 in range(1, 11):
        print(f"{i} x {i2} = {i * i2}")

#negócio de linhas
n = int(input("Digite a quantidade de linhas: "))

for i in range(1, n + 1):
    for i2 in range(1, i + 1):
        print(i2, end=" ")
    print()