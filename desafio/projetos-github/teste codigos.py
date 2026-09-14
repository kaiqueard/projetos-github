matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
]
# # matriz[0][0] = 1
# # matriz[0][1] = 2
# # matriz[0][2] = 3
# # matriz[1][0] = 4
# # matriz[1][1] = 5
# # matriz[1][2] = 6
# # matriz[2][0] = 7
# # matriz[2][1] = 8
# # matriz[2][2] = 9

# # print(matriz)

# # for row in matriz:
# #     print(row)

# #mesma coisa que
# # for row in range(3)
# # print(matriz[row])  

# for linha in range(3):
#     for coluna in range(3):
#         print(matriz[linha][coluna])  

matriz[0][0] = 20
matriz[1][2] = 15
matriz[2][1] = 19

# print(matriz)

# for linha in range(3):
#     print(matriz[linha])

# for linha in range(3):
#     for coluna in range(3):
#         print(matriz[linha][coluna])

soma = matriz [0][0] + matriz[1][0]
sub = matriz[2][2] - matriz[2][1]
mult = matriz[0][1] * matriz[2][0]
div = matriz [1][2] / matriz[0][2]

print(
    soma,
    sub,
    mult,
    div
)