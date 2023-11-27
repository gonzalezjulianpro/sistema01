import menu
import os


def cadastro_pessoa_main():  #Fucao principal de chamadas
    print("Menu Cadastro de Pessoas")
    opcao = input("1 - Criar Nova Lista\n2 - Adicionar em Lista já existente\n3 - Conferir Lista Existente\n0 - Voltar para Menu Principal\nOpcao: ")
    opcao = int(opcao.strip())

    if(opcao == 1):
        criar_lista()
    elif(opcao == 2):
        adiciona()
    elif(opcao == 3):
        confere_listas()
    elif(opcao == 0):
        menu.iniciando()#volta para o Menu Principal
    else:
        print("\nOpcao invalida. Tente Novamente\n")
        cadastro_pessoa_main()


def criar_lista():#Criando arquivo de banco de dados txt

    print("\nCriacao Banco de Dados TXT")
    banco_dado = input("Insira o nome do banco de dados para criacao, com 'BD' no final.\nEx: bancoBD\nNome: ")
    banco_dado = banco_dado.strip()
    print("Nome do Banco de Dados: {}.txt".format(banco_dado))
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

def adiciona():#funcao de adicao de pessoa no sistema

    diretorio = input("Insira o caminho completo do diretorio utilizado: ").strip()
    chama_banco = input("Insira o nome do banco desejado: ").strip()
    teste_mensagem = input("Escreve mensagem de teste: \n") #Testando escrita em arquivo
    with open("{}{}.txt".format(diretorio, chama_banco), "a") as escreve_banco:
        escreve_banco.write("\n{}".format(teste_mensagem))
        escreve_banco.close()
    cadastro_pessoa_main()


def confere_listas():#Lista todos os bancos que já foram criados

    diretorio = input("Insira o caminho completo do diretorio utilizado: ").strip()
    file_end = "BD.txt"
    menu.pulaLinha()
    print("Bancos:")
    for file in os.listdir(diretorio):
        if file.endswith(file_end):
            print(os.path.join(diretorio, file))
    menu.pulaLinha()
    cadastro_pessoa_main()


if(__name__ == "__main__"):
    cadastro_pessoa_main()