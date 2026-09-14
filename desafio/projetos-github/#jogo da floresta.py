#jogo da floresta

print("Você está em uma floresta e precisa escolher um caminho para seguir. Você pode escolher: esquerda ou direita")
lado = input("Escolha para qual lado você quer ir (esquerda/direita): ").lower()
if lado == "esquerda":
    lado2 = input("Você encontrou um RIO, escolha: atravessar/voltar: ").lower()
    if lado2 == "atravessar":
        print("Você achou uma vila segura")
    elif lado2 == "voltar":
        print("Você permanece perdido na floresta")


elif lado == "direita":
    lado3 = input("Você encontrou uma MONTANHA, escolha: subir/voltar ").lower()
    if lado3 == "subir":
        print("Você encontrou um tesouro")
    elif lado3 == "voltar":
        print("você permanece perdido na floresta")
#foi o mais divertido de fazer, a professora explicou muito bem, porém eu me bati um pouco para fazer os "voltar" (os lower nao funcionam)


#verificar numero
numero = int(input("\n Digite um número inteiro: "))
if numero < 10:
    print("Seu número é menor que 10")
elif numero >= 10 and numero <= 50:
    print("Seu número esta entre 10 e 50")
else:
    print("Seu número é maior que 50")


#verificar se o ano é bissexto
ano = int(input("\nDigite um ano: "))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    #aqui eu poderia ter botado "if ano % 4 == 0 and ano % 400 == 0
    print("Seu ano é bissexto")
else:
    print("Seu ano não é bissexto")


#pedir ao usuario senha
conta = input("\n Digite seu nome de usuário: ")
senha = input("Digite sua senha: ")
if conta == "admin" and senha == "1234":
    print("Acesso permitido")
    #ele ainda pede a senha porem por ser 'convidado' sempre seria acesso restrito
elif conta == "convidado":
    print("Acesso restrito")
else:
    print("Acesso bloqueado")

#verificar coordenadas
x = float(input("\n Digite sua coordenada X: "))
y = float(input(" Digite sua coordenada Y: "))
if x > 0 and x < 10 and y > 0 and y < 10:
    print('dentro do quadrado')
elif (x == 0 or x == 10) and (0 <= y <= 10) or (y == 0 or y == 10) and (0 <= x <= 10):
    print("na fronteira")
else:
    print('fora do quadrado')
#dificil, na parte do elif foi muito complicado