#LISTA LISTA]
import random

#1
lista = list() #escrevendo assim para nao confundir com vetor, podia usar "[]"
numero = 0
for i in range(10):
    numero = random.randint(1,100)
    lista.append(numero)
print(lista)

#2
lista = list()
for i in range(3):
    numero = int(input("Digite seu núemro: "))
    lista.append(numero)
print(lista)

#3
palavra = input("Digite sua frase: ")
lista = palavra.split() #split separa nos espaços, bom saber

print(lista)

#4
lista = list()
for i in range(10):
    i += 1
    lista.append(i)
lista.reverse() #bati a cabeça para fazer essa.
print(lista)

#5
frase = input("Digite sua frase para dividir em palavras: ") #peço a frase

lista = frase.split() #boto em uma lista, separando por palavra

menor = min(lista, key = len) #tiro o minimo e o maximo(maior e menor) e determino q o parâmetro de medida é len pela key
maior = max(lista, key = len)

#printo
print("Palavras: ", lista)
print("Menor palavra: ", menor)
print("Maior palavra: ", maior)

#6
lista_par = list()
lista_impar = list()
lista_junto = list()
for i in range(10):
    i += 1 #pra nao printar o zero
    if i % 2 == 0:
        lista_par.append(i)
    elif i % 2 == 1:
        lista_impar.append(i)
lista_junto = lista_par + lista_impar #nao sabia que dava pra somar duas listas e ficar assim
print(lista_junto)

#7
lista_par = list()
# lista = list()
for i in range(1,101):
    # lista.append(i) #mesmo resultado
    if i % 2 == 0:
        lista_par.append(i)
print(lista_par)

#8
lista = list()
for i in range(1,11):
    i = i ** 2
    lista.append(i)
lista = sum(lista)
print(lista)

#9
alfabeto = ("abcdefghijklmnopqrstuvwxyz")
lista = list(alfabeto)
random.shuffle(lista) #comando novo pra misturar a lista, somente lista
#print(lista)
tentativa = int(input("Tente achar a posição em que se encontra a letra 'K' 0-25: "))
if lista[tentativa] == 'k':
    print('Parabéns, Correto!')
elif lista[tentativa] != 'k':
    print("Errado!")
print(lista)

#10 jogo da velha
mapa = [" "] * 9
jogador = "X"

while True:
    print(mapa[0], mapa[1], mapa[2])
    print(mapa[3], mapa[4], mapa[5])
    print(mapa[6], mapa[7], mapa[8])

    print("Jogador", jogador)

    jogada = int(input("Qual sua jogada (0-8): "))

    if mapa[jogada] != " ":
        print("Posição ocupada!")
        continue

    mapa[jogada] = jogador

    if jogador == "X":
        jogador = "O"
    else:
        jogador = "X"











