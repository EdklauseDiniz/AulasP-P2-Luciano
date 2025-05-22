"""Questão 06"""
"""num = input("Digite um número inteiro: ")
num = int(num)
modulo = num % 2
if modulo == 0:
    print("O número digitado é par.")
else:
    print("O número digitado é impar.")"""

"""Questão 07"""
"""def aprovado(nota1,nota2,nota3):
    media = (nota1+nota2+nota3)/3
    if media < 4:
        print("Você está reprovado")
    elif media >= 4 and media < 7:
        print("Você vai para prova final")
    else:
        print("Você está aprovado")

nota1 = input("Digite a primeira nota: ")
nota1 = nota1.replace(",",".")
nota1 = float(nota1)
nota2 = input("Digite a segunda nota: ")
nota2 = nota2.replace(",",".")
nota2 = float(nota2)
nota3 = input("Digite a terceira nota: ")
nota3 = nota3.replace(",",".")
nota3 = float(nota3)
aprovado(nota1,nota2,nota3)"""

"""Questão 08"""
"""def classificacao(idade):
    if idade >= 5 and idade <=7:
        print("Ele vai fazer parte da competição junior")
    elif idade >= 8 and idade <=12:
        print("Ele vai fazer parte da competição infantil")
    elif idade >= 13 and idade <=18:
        print("Ele vai fazer parte da competição pré")
    elif idade > 18:
        print("Ele vai fazer parte da competição avançada")

idade = input("Digite a idade do nadador: ")
idade = int(idade)
classificacao(idade)"""

"""Questão 09"""
"""
Não esquece de botar os ","" lá
def adicao(num1,num2):
    conta = num1+num2
    print("O primeiro número é:"+str(num1))
    print("O segundo número é:"+str(num2))
    print("E a soma deles é:"+str(conta))

def subtracao(num1,num2):
    conta = num1-num2
    print("O primeiro número é:"+str(num1))
    print("O segundo número é:"+str(num2))
    print("E a subtração do número 1 pelo número 2 é:"+str(conta))

def divisao(num1,num2):
    if num1 == 0 and num2 == 0:
        print("Não é possível dividir zero por zero")
        return
    elif num2 == 0:
        print("Não da para dividir por 0")
        return
    conta = num1/num2
    print("O primeiro número é:"+str(num1))
    print("O segundo número é:"+str(num2))
    print("E a divisão do número 1 pelo número 2 é:"+str(conta))

def multiplicacao(num1,num2):
    conta = num1*num2
    print("O primeiro número é:"+str(num1))
    print("O segundo número é:"+str(num2))
    print("E a multiplicação deles é:"+str(conta))

num1 = input("Digite o primeiro número: ")
num1 = num1.replace(",",".")
num1 = float(num1)
sinal = input(
Digite o sinal da operação:
+ = Adição;
- = Subtração;
/ = Divição;
* = Multiplicação.
Sinal: )
sinal = sinal.replace(" ","")
num2 = input("Digite o segundo número: ")
num2 = num2.replace(",",".")
num2 = float(num2)
if sinal == "+":
    adicao(num1,num2)
elif sinal == "-":
    subtracao(num1,num2)
elif sinal == "/":
    divisao(num1,num2)
elif sinal == "*":
    multiplicacao(num1,num2)
else:
    print("O sinal escolhido não é suportado.")
"""
"""Questão 10"""
"""
def organizacao(num1,num2,num3):
    ord1 = 0
    ord2 = 0
    ord3 = 0

    if num1 < num2 and num1 < num3:
        ord1 = num1
    elif num1 < num2 and num1 > num3:
        ord2 = num1
    elif num1 > num2 and num1 < num3:
        ord2 = num1
    elif num1 > num2 and num1 > num3:
        ord3 = num1

    if num2 < num1 and num2 < num3:
        ord1 = num2
    elif num2 < num1 and num2 > num3:
        ord2 = num2
    elif num2 > num1 and num2 < num3:
        ord2 = num2
    elif num2 > num1 and num2 > num3:
        ord3 = num2 

    if num3 < num2 and num3 < num1:
        ord1 = num3
    elif num3 < num2 and num3 > num1:
        ord2 = num1
    elif num3 > num2 and num3 < num1:
        ord2 = num3
    elif num3 > num2 and num3 > num1:
        ord3 = num3 
    print(ord1,ord2,ord3)

num1 = input("Digite o primeiro número: ")
num1 = num1.replace(",",".")
num1 = float(num1)
num2 = input("Digite o segundo número: ")
num2 = num2.replace(",",".")
num2 = float(num2)
num3 = input("Digite o terceiro número: ")
num3 = num3.replace(",",".")
num3 = float(num3)

organizacao(num1,num2,num3)
"""
"""Questão 11"""

"""Questão 12"""