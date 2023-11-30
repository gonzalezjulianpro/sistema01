import cadastro_nova_pessoa
import menu
import csv
import verifica_pessoa

def deleta_pessoa_main():
    print("***Menu de exclusao de pessoas***")
    opcao = int(input("1 - Listar bancos disponiveis.\n2 - Deletar todos os dados da lista.\n3 - Deletar dados de pessoa especifica.\n0 - Voltar ao Menu anterior.\n Opcao: ").strip())

    if(opcao == 1):
        cadastro_nova_pessoa.confere_listas()
    elif(opcao == 2):
        deleta_tudo()
    elif(opcao == 3):
        deleta_especifico()
    elif(opcao == 0):
        menu.iniciando()
    else:
        print("\nOpcao invalida. Tente Novamente\n")
        deleta_pessoa_main()


def deleta_tudo(): #funcao apaga todos os dados do banco csv
    caminho = input("Por favor digite o caminho completo para o banco que sera excluido: ")
    menu.pulaLinha()
    alerta = input("Realmente deseja apagar os dados do banco?\n(S/N): ")
    alerta = alerta.upper()
    if (alerta == "S"):
        with open(caminho, "w") as banco:
            banco.write("")
            banco.close()
        print("Banco '{}' foi deletado com sucesso!".format(caminho))
        menu.pulaLinha()
        menu.iniciando()
    elif (alerta == "N"):
        print("Operacao cancelada!")
        menu.pulaLinha()
        deleta_pessoa_main()
    else:
        print("Opcao invalida. Retornando ao Menu anterior.")
        menu.pulaLinha()
        deleta_pessoa_main()


def deleta_especifico(): #funcao para deletar linha especifica do csv
    caminho = input("Por favor digite o caminho completo para o banco que sera excluido: ")
    nome = input("O dado de quem sera apagado?\nNome: ")
    lista = []
    with open(caminho, "r") as banco:
        leitor = csv.reader(banco)
        for linha in leitor:
            while(linha[0] != nome):
                lista = linha
                with open(caminho, "w") as new_banco:
                    escritor = csv.writer(new_banco)
                    escritor.writerow(linha)
                new_banco.close()
        banco.close()
    print("Dado apagado com sucesso!")
    menu.pulaLinha()
    deleta_pessoa_main()

'''def deleta_especifico(): #funcao para deletar linha especifica do csv
    caminho = input("Por favor digite o caminho completo para o banco que sera excluido: ")
    menu.pulaLinha()
    nome = input("O dado de quem sera apagado?\nNome: ")
    lista = []
    with open(caminho, "r") as in_file, open(caminho, "w") as out_file:
        reader = csv.reader(in_file)
        writer = csv.writer(out_file)

        for linha in reader:
            if(linha[0] != nome):
                writer.writerow(linha)
            else:
                pass
        in_file.close()
        out_file.close()'''


if(__name__ == "__main__"):
    deleta_pessoa_main()