#exercicios funçoes
#1 
def soma_elementos(lista):
    return sum(lista)
print(soma_elementos([1,2,3,4,5]))

#2
def e_palindromo(texto):
    return texto == texto[::-1]

print(e_palindromo("arara"))
print(e_palindromo("roblox"))

#3
def maior_elemento(lista):
    return max(lista)
print(maior_elemento([1,2,3,4,5]))

#4
def contar_caracteres(a,x):
    contador = 0
    for letra in a:
        if letra == x:
            contador += 1
    return contador
print(contar_caracteres("abacate", "a"))

##5
def soma(a,x):
    return a + x

def sub(a,x):
    return a - x

def mult(a,x):
    return a * x

def div(a,x):
    return a / x

def menu():
    print()
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("0 - Sair")
    print()

while True:
    menu()
    opcao = int(input("Escolha uma opção: "))
    if opcao == 0:
        print("Saindo...")
        break

    a = int(input("Digite seu primeiro número: "))
    x = int(input("Digite seu segundo número: "))

    if opcao == 1:
        print(soma(a,x))
    elif opcao == 2:
        print(sub(a,x))
    elif opcao == 3:
        print(mult(a,x))
    elif opcao == 4:
        print(div(a,x))
    else:
        print("Opção inválida")