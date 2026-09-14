#lista vetores

#1 

A = [1, 0, 5, -2, -5, 7]
soma = A[0] + A[1] + A[5]
print(soma)

A[4] = 100
print(A[0])
print(A[1])
print(A[2])
print(A[3])
print(A[4])
print(A[5])

#2

numeros = [0,0,0,0,0,0]
for i in range (0,6,1):
    numeros[i] = int(input("Digite seu numero: "))
print(numeros)

#3
numeros = [0,0,0,0,0,0,0,0,0,0]
quadrados = [0,0,0,0,0,0,0,0,0,0]
for i in range (0,10,1):
    numeros[i] = float(input("Digite seu numero: "))
    quadrados[i] = numeros[i] ** 2
print(numeros)
print(quadrados)

#4
numeros = [0,0,0,0,0,0,0,0]
for i in range(8):
    numeros[i] = int(input("Digite um numero: "))
x = int(input("Digite a posição do x, 0-7: "))
y = int(input("Digite a posição do y, 0-7: "))

soma = numeros[x] + numeros[y]
print("Soma dos valores x e y é: ", soma)

# #5
vetor = [0,0,0,0,0,0,0,0,0,0]
par = 0
for i in range(10):
    vetor[i] = int(input("Digite seu número: "))
    if vetor[i] % 2 == 0:
        par += 1
print("números pares: ", par)

#6
vetor = [0,0,0,0,0,0,0,0,0,0]
maior = vetor[0]
menor = vetor[0]
for i in range(10):
    vetor[i] = int(input("Digite seu número: "))

for i in range(10):
    if vetor[i] > maior:
        maior = vetor [i]
    elif vetor[i] < menor:
        menor = vetor [i]

print("menor: ", menor)
print("maior", maior)

#7
vetor = [0,0,0,0,0,0,0,0,0,0]
maior = vetor[0]
posicao = 0
for i in range(10):
    vetor[i] = int(input("Digite seus números: "))

for i in range(10):
    if vetor[i] > maior:
        maior = vetor[i]
        posicao = i
    
print(vetor)
print(maior)
print(posicao)

#8
vetor = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
media = 0
for i in range(15):
    vetor[i] = float(input("Digite sua nota: "))

for i in range(15):
    media += vetor[i]

media = media / 15
print("A média geral é: ", media) 

#9
vetor = [0,0,0,0,0,0,0,0,0,0]
negativos = 0
soma = 0
for i in range(10):
    vetor[i] = float(input("Digite seus números: "))

for i in range(10):
    if vetor[i] < 0:
        negativos += 1
    elif vetor[i] > 0:
        soma += vetor[i]

print("quantidade de negativos: ", negativos)
print("soma dos positivos: ", soma)

#10
vetor = [0,0,0,0,0]
maior = vetor[0]
menor = vetor[0]
media = 0
for i in range(5):
    vetor[i] = int(input("Digites seus numeros: "))
    media += vetor[i]

for i in range(5):
    if vetor[i] > maior:
        maior = vetor[i]
    elif vetor[i] < menor:
        menor = vetor[i]

media = media / 5
print(vetor)
print("menor numero é: ", menor)
print("maior numuro é: ", maior)
print("Sua média é: ", media)

#11
vetor = [0,0,0,0,0]
maior = vetor[0]
menor = vetor[0]
posicao1 = 0
posicao2 = 0
for i in range(5):
    vetor[i] = int(input("Digite seus valores: "))

for i in range(5):
    if vetor[i] > maior:
        maior = vetor[i]
        posicao1 = [i] 

    elif vetor[i] < menor:
        menor = vetor[i]
        posicao2 = [i] 

print("posição do maior número é: ", posicao1)
print("posição do menor número é: ", posicao2) 

    



    