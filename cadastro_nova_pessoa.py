import menu

def cadastro_pessoa_main():  #Fucao principal de chamadas
    print("Menu Cadastro de Pessoas")
    opcao = input("1 - Criar Nova Lista\n2 - Adicionar em Lista já existente\n0 - Voltar para Menu Principal\nOpcao: ")
    opcao = int(opcao.strip())

    if(opcao == 1):
        criar_lista()
    elif(opcao == 2):
        adiciona()
    elif(opcao == 0):
        menu.iniciando()
    else:
        print("\nOpcao invalida. Tente Novamente\n")
        cadastro_pessoa_main()

def criar_lista():#Criando arquivo de banco de dados txt
    print("\nCriacao Banco de Dados TXT")
    banco_dado = input("Insira o nome do banco de dados para criacao\nNome: ")
    banco_dado = banco_dado.strip()
    confirmacao = input("1 - O nome esta correto\n2 - O nome esta incorreto\nOpcao: ")#Confirmacao para criacao de banco
    confirmacao = int(confirmacao.strip())
    if(confirmacao == 1):
        arquivo = open("{}.txt".format(banco_dado), "w") #comando para criar o arquivo .txt com o nome escolhido pelo usuario
        arquivo.close()
        cadastro_pessoa_main()
    else:
        confirmacao2 = input("1 - Tentar Novamente\n2 - Voltar ao Menu Anterior\nOpcao: ")#Confirmacao para nova criacao de banco, tentar novamente?
        confirmacao2 = int(confirmacao2.strip())
        if(confirmacao2 == 1):
            print("!!!Nova Tentativa de Criacao de Banco de Dados TXT!!!")
            criar_lista()
        elif(confirmacao2 == 2):
            print("!!!Retornando ao Menu anterior!!!")
            cadastro_pessoa_main()
        else:
            print("Opcao invalida!\nRedirencionando para automaticamente para o Menu anterior.")
            cadastro_pessoa_main()

def adiciona():
    print("A funcao adiciona funciona!")


if(__name__ == "__main__"):
    cadastro_pessoa_main()