#teste funçao
#1
def imprimir_nome():
    nome = "kaique"
    print(nome)
imprimir_nome()

#2
def maior(x,z,y):
    if x > z and x > y:
        return x
    elif z > x and z > y:
        return z
    elif y > x and y > z:
        return y
print(maior(2,4,10))

#3
def criar_vetor():
    a = [0] * 5
    return a
#ou
#vetor = criar_vetor()
#print(vetor)
print(criar_vetor())

#4
def media(lista):
    return sum(lista) / len(lista)
print(media(lista = [1,2,3,4,5]))

#5
def inverter(texto):
    resultado = " "

    for letra in texto:
        resultado = letra + resultado

    return resultado

print(inverter("roblox"))

#6
matriz = []

for i in range(3):
    linha = []
    for j in range(3):
        valor = int(input("Digite valor: "))
        linha.append(valor)
    matriz.append(linha)

print("Diagonal principal:")

for i in range(3):
    print(matriz[i][i])






