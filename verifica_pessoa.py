import cadastro_nova_pessoa
import menu
import pandas as pd
import csv

def verifica_pessoa_main():
    print("***Menu de verificacao de pessoas***")
    opcao = int(input("1 - Listar bancos disponiveis\n2 - Listar todos os cadastros em lista especifica\n3 - Lista dados de pessoa especifica\n0 - Voltar ao Menu anterior\n Opcao: ").strip())

    if (opcao == 1):
        cadastro_nova_pessoa.confere_listas()

    elif (opcao == 2):
        todos_cadastros()

    elif (opcao == 3):
        pessoa_especifica()

    elif (opcao == 0):
        menu.iniciando()
    else:
        print("\nOpcao invalida. Tente Novamente\n")
        verifica_pessoa_main()


'''
def todos_cadastros():# leitura de banco csv
    banco = input("Passe o caminho completo do banco: ").strip()
    with open("{}".format(banco), "r") as mostra_banco: #abertura do arquivo csv em modo de leitura
        dado = csv.reader(mostra_banco)
        for linha in dado: #impressao linha por linha do arquivo csv

            print(linha)
    mostra_banco.close()
'''
def todos_cadastros():# leitura de banco csv
    caminho = input("Passe o caminho completo do banco: ").strip()
    menu.pulaLinha()
    banco = pd.read_csv(caminho) #abertura do arquivo csv em modo de leitura
    banco.columns = ["Nome", "Idade", "Profissao", "Status"] #criando colunas para exibicoa do arquivo de banco csv
    print(banco)
    menu.pulaLinha()
    print("!!!Retornando ao Menu anterior!!!")
    menu.pulaLinha()
    verifica_pessoa_main()


def pessoa_especifica():# leitura no banco csv com insercao de pessoa especifica
    caminho = input("Passe o caminho completo do banco: ").strip()
    nome = input("Insira o nome desejado: ").strip()
    lista = []
    menu.pulaLinha()

    with open(caminho, "r") as banco: #abrindo e efetuando a leitra do banco csv
        leitor = csv.reader(banco)
        for linha in leitor:
            if(linha[0] == nome): #adicionando a linha do csv em uma lista para impressao solicitada
                lista = linha
        banco.close()

    print("***Dado Selecionado:***")
    print ("Nome: {}\nIdade: {}\nProfissao: {}\nEstado Civil: {}".format(lista[0],lista[1],lista[2],lista[3]))
    menu.pulaLinha()

    comando = int(input("1 - Fazer nova consulta.\n2 - Voltar ao Menu anterior.\n0 - Sair do programa.\nOpcao: ").strip())

    if(comando == 1):
        pessoa_especifica()
    elif(comando == 2):
        verifica_pessoa_main()
    elif(comando == 0):
        exit()
    else:
        print("!!!Voce nao digitou um valor valido. Retornando ao Menu Principal!!!")
        menu.iniciando()



if(__name__ == "__main__"):
    verifica_pessoa_main()