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
    caminho = input("Por favor digite o caminho completo para o banco que sera excluido: ").strip()
    nome_input = input("O dado de quem sera apagado?\nNome: ").strip()
    column_name = "Nome"#fixei por nome, porem pode ser colocado condicao para selecao
    index_to_remove = None

    with open(caminho, "r") as banco_leitura: #Leitura do arquivo
        reader = csv.DictReader(banco_leitura, delimiter=";")
        rows = list(reader)

        for i,row in enumerate(rows):

            if row[column_name] == nome_input:
                dado = row
                index_to_remove = i
                break

    banco_leitura.close()#fechando arquivo de leitura
    if index_to_remove is not None:
        removed_row = rows.pop(index_to_remove)#removendo linha escolhida

        with open(caminho, "w", newline="") as banco_escrita:#iniciando sobrescricao
            writer = csv.DictWriter(banco_escrita, fieldnames=reader.fieldnames, delimiter=";")
            writer.writeheader()
            writer.writerows(rows)

    else:
        print("Linha não encontrada --- {}: {}".format(column_name, nome_input))

    banco_escrita.close()#fechando arquivo escrita
    print("Dado apagado com sucesso: {}".format(dado))
    menu.pulaLinha()
    deleta_pessoa_main()


if(__name__ == "__main__"):
    deleta_pessoa_main()