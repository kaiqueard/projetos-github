# crescente
for i in range(1,11):
    print(i)

# decrescente
for i in range (10,0,-1):
    print(i)

# printar par ou impar até 10(podia usar o "continue", e tal)
for i in range(1,11):
    if i % 2 == 0:
        print("Par", i)
    else:
        print("Impar", i)

#for para palavra (poderia usar "startswith")
palavra = input("Digite sua palavra que comece com vogal: ")

while palavra[0].lower() != 'a' or palavra[0].lower() != 'e' or palavra[0].lower() != 'i' or palavra[0].lower() != 'o' or palavra[0].lower() != 'u':
    print("Palavra invalida: ")
    palavra = input("Digite sua palavra novamente")
for letra in palavra:
    print(letra)