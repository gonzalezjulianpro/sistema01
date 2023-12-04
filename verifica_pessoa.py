import cadastro_nova_pessoa
import menu
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

def todos_cadastros():# leitura de banco csv
    caminho = input("Passe o caminho completo do banco: ").strip()
    menu.pulaLinha() #FAZER NOVA IMPLEMENTACAO USANDO LIB CSV
    with open(caminho, "r") as banco:
        reader = csv.reader(banco, delimiter=";")
        for row in reader:
            print(row)
        banco.close()
    menu.pulaLinha()
    print("!!!Retornando ao Menu anterior!!!")
    verifica_pessoa_main()


def pessoa_especifica():# leitura no banco csv com insercao de pessoa especifica
    caminho = input("Passe o caminho completo do banco: ").strip()
    nome = input("Insira o nome desejado: ").strip()
    column_name = "Nome"#defini a pesquisa por nome, porem pode ser criado condicoes para pesquisa por qualquer campo
    lista = []
    menu.pulaLinha()

    with open(caminho, "r") as banco_reader: #abrindo arquivo
        reader = csv.DictReader(banco_reader, delimiter=";") #criando leitor
        rows = list(reader) #colocando as linhas em sequencia
        for row in rows:
            #print(rows)
            if (row[column_name] == nome):
                lista = row
                print("Resultado: {}".format(lista))
        banco_reader.close()
    #print("Resultado: {}".format(lista))
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