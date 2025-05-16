jogos = []

def exibir_menu():
    print('''
    Escolha uma opção:  
    
    1 - Adicione um jogo;
    2 - Remova um jogo;
    3 - Altere uma informação;
    4 - Consulte um jogo;
    0 - Sair do sistema.
    ''')

def adicionar():
    nome = input("Qual o nome do jogo: ")
    preco = input("Qual o preço do jogo: ")
    preco = preco.replace(",",".")
    preco = float(preco)
    criador = input("Qual o nome do criador do jogo: ")
    data = input("Qual o ano de lançamento do jogo: ")
    data = int(data)
    jogo = {
        "nome": nome,
        "preco": preco,
        "criador": criador,
        "data": data
    }
    jogos.append(jogo)

def remover():
    x = 0
    print("Qual jogo você quer remover")
    for x in (len(jogos)-1):
        txt = " - "+
        print(x+)