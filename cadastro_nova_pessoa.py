import menu
import os
import pandas as pd
import csv

def cadastro_pessoa_main():  #Fucao principal de chamadas
    print("***Menu Cadastro de Pessoas***")
    opcao = int(input("1 - Criar Nova Lista\n2 - Adicionar em Lista já existente\n3 - Conferir Lista Existente\n0 - Voltar para Menu Principal\nOpcao: ").strip())

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

    print("\nCriacao Banco de Dados CSV")
    banco_dado = input("Insira o nome do banco de dados para criacao, com 'BD' no final.\nEx: bancoBD\nNome: ")
    banco_dado = banco_dado.strip()
    print("Nome do Banco de Dados: {}.csv".format(banco_dado))
    confirmacao = input("1 - O nome esta correto\n2 - O nome esta incorreto\nOpcao: ")#Confirmacao para criacao de banco
    confirmacao = int(confirmacao.strip())
    if(confirmacao == 1):
        with open("{}.csv".format(banco_dado), "w", newline="") as arquivo:
            fieldname = ["Nome", "Idade", "Profissao", "Status"]
            writer = csv.DictWriter(arquivo,fieldnames=fieldname, delimiter=";")
            writer.writeheader()
            arquivo.close()
            cadastro_pessoa_main()
    else:
        confirmacao2 = input("1 - Tentar Novamente\n2 - Voltar ao Menu Anterior\nOpcao: ")#Confirmacao para nova criacao de banco, tentar novamente?
        confirmacao2 = int(confirmacao2.strip())
        if(confirmacao2 == 1):
            print("!!!Nova Tentativa de Criacao de Banco de Dados CSV!!!")
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
    print("Banco Escolhido: {}{}.csv".format(diretorio, chama_banco))
    confirma = int(input("1 - O banco esta correto.\n2 - O banco esta incorreto.\nOpcao: "))# primeira confirmacao necessaria

    if (confirma == 1):
        print("*** Novo Cadastro ***")
        nome = input("Nome: ")
        idade = input("Idade: ")
        profissao = input("Profissao: ")
        status_civil = input("Status Civil: ")
        with open("{}{}.csv".format(diretorio, chama_banco), "a") as escreve_banco: # Escrevendo no arquivo
            fieldname = ["Nome", "Idade", "Profissao", "Status"]
            writer = csv.DictWriter(escreve_banco, fieldnames=fieldname, delimiter=";")
            writer.writerow({"Nome": nome, "Idade": idade, "Profissao": profissao, "Status": status_civil})
            escreve_banco.close()
        print("Cadastro Realizado com Sucesso!!!")
        cadastro_pessoa_main()
    elif (confirma == 2):
        confirma2 = int(input("1 - Tentar novamente.\n2 - Cancelar e retornar ao Menu anterior\nOpcao: "))# Segunda confirmacao necessaria
        if (confirma2 == 1):
            print("!!!Nova tentativa!!!")
            menu.pulaLinha()
            adiciona()
        elif (confirma2 == 2):
            print("Cancelando registro. Retornando ao Menu anterior!")
            menu.pulaLinha()
            cadastro_pessoa_main()
        else:
            print("Opcao invalida. Retornando ao Menu Principal.")
            menu.pulaLinha()
            menu.iniciando()
    else:
        print("Opcao invalida. Retornando ao Menu anterior!")
        menu.pulaLinha()
        cadastro_pessoa_main()



def confere_listas():#Lista todos os bancos que já foram criados

    diretorio = input("Insira o caminho completo do diretorio utilizado: ").strip()
    file_end = "BD.csv"
    menu.pulaLinha()
    print("Bancos:")
    for file in os.listdir(diretorio):
        if file.endswith(file_end):
            print(os.path.join(diretorio, file))
    menu.pulaLinha()
    cadastro_pessoa_main()


if(__name__ == "__main__"):
    cadastro_pessoa_main()