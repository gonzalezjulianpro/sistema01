import cadastro_nova_pessoa
import verifica_pessoa
import  deleta_pessoa


def iniciando(): #funcao principal
    print("Menu:\n")
    comando = menu_apresentacao()  # print("Você selecionou o: {}".format(comando)) --- TESTE FUNCAO "menu_apresentacao()"

    if(comando == 1):
        #print("1 - valido") #teste validação
        cadastro_nova_pessoa.cadastro_pessoa_main()#chamada de cadastro
    elif(comando == 2):
        #print("2 - valido") #teste validação
        verifica_pessoa.verifica_pessoa_main()
    elif(comando == 3):
        #print("3 - valido") #teste validação
        deleta_pessoa.deleta_pessoa_main()
    elif(comando == 0):
        exit()
    else:
        print("\nVoce inseriu uma opcao invalida!\n")
        tentativa()


def menu_apresentacao(): #funcao de apresentacao inicial do menu
    comando = input("1 - Cadastrar Nova Pessoa\n2 - Verificar Pessoas Cadastradas\n3 - Deletar Pessoa Cadastrada\n0 - Sair do Programa\nOpcao: ").strip()
    return int(comando)

def tente_novamente_tentativa(): #funcao para nova tentativa da funcao tentativa()
    print("Opcao invalida!\nTente novamente!\n")
    tentativa()

def tentativa(): #nova tentativa de opcao invalida
    tentativa = input("1 - Deseja tentar novamente.\n0 - Deseja Sair do Programa\nOpcao: ")
    tentativa = int(tentativa.strip())

    if(tentativa == 1):
        iniciando()
    if(tentativa == 0):
        exit()
    else:
        tente_novamente_tentativa()

def pulaLinha():  # funcao auxiliar para pular linhas
    print("\n")


if(__name__ == "__main__"):
    iniciando()