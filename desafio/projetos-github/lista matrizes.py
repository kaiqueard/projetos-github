#1
matriz = [
    [1,0,0,0,0],
    [0,1,0,0,0],
    [0,0,1,0,0],
    [0,0,0,1,0],
    [0,0,0,0,1]
]

print(matriz)
#OU
matriz = [
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0]
]
for i in range(5):
    for j in range(5):
        if i == j:
            matriz[i][j] = 1
        else:
            matriz[i][j] = 0
print(matriz)

#2
matriz = [
    [0,0,0,0,],
    [0,0,0,0,],
    [0,0,0,0,],
    [0,0,0,0,]
]
for i in range(4):
    for j in range(4):
        valor = int(input("Digite um valor: "))
        matriz[i][j] = valor
print(matriz)

maior = matriz[0][0]
linha_maior = 0
coluna_maior = 0
for i in range(4):
    for j in range(4):
        if matriz[i][j] > maior:
            linha_maior = i
            coluna_maior = j
print("O maior valor esta na posição", linha_maior, coluna_maior)

#3
matriz = [
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0]
]
for i in range(5):
    matriz[i][0] = int(input("Matricula: "))
    matriz[i][1] = int(input("media das provas: "))
    matriz[i][2] = int(input("media dos trabalhos: "))
    matriz[i][3] = matriz[i][1] + matriz[i][2]

maior = matriz[0][3]
matricula_maior = matriz[0][0]

for i in range(5):
    if matriz[i][3] > maior:
        maior = matriz[i][3]
        matricula_maior = matriz[i][0]

print("matricula com maior nota:", matricula_maior)







