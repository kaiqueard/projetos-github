# 1 - Calcular idade
ano_nascimento = int(input("Digite seu ano de nascimento: "))
ano_atual = int(input("Digite o ano atual: "))
idade = ano_atual - ano_nascimento
print("Sua idade é:", idade)


# 2 - Locadora de carros
quantidade = int(input("\nQuantos carros deseja alugar? "))
preco_carro = 100
total = quantidade * preco_carro
print("Valor total da locação: R$", total)


# 3 - Celsius para Fahrenheit
celsius = float(input("\nDigite a temperatura em Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print("Temperatura em Fahrenheit:", fahrenheit)


# 4 - Média de 4 notas
n1 = float(input("\nDigite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))
n4 = float(input("Digite a quarta nota: "))
media = (n1 + n2 + n3 + n4) / 4
print("A média é:", media)


# 5 - Idade em meses
idade_anos = int(input("\nDigite sua idade em anos: "))
meses = idade_anos * 12
print("Sua idade em meses é:", meses)


# 6 - Preço de venda por quilo
preco_quilo = float(input("\nDigite o preço por quilo: "))
peso = float(input("Digite o peso em kg: "))
total = preco_quilo * peso
print("Preço total: R$" , total)