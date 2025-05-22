"""Questão 12"""

def questao12():
    idademenor = 999999999999999999999999999999999999
    idademaior = 0
    velho = ""
    jovem = ""
    while True:
        idade = input("Digite a idade de uma pessoa: ")
        idade = int(idade)
        if idade == 0:
            break
        nome = input("Digite o nome dessa pessoa: ")
        if idade < idademenor:
            idademenor = idade
            jovem = nome
        if idade > idademaior:
            idademaior = idade
            velho = nome
    print("A/s maior/es idade/s foi/foram de: "+velho)
    print("A/s menor/es idade/s foi/foram de: "+jovem)

questao12()