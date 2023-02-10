# Importando os módulos do S.O.(Sistema Operacional)
import os, sys  # Não retire o sys!, ele esta sendo usando dentro do Dicionário

# importações necessárias para carregar os módulos da Aplicação:
from inclusaoProd import *
from menuAlteracao import *
from exclusao import *
from menuRelatorios import *

# Função do Menu principal
def menu():
    print('=' * 50)
    print("1 - Inclusão de Dados")
    print("2 - Alteração de Dados")
    print("3 - Exclusão de Dados")
    print("4 - Relatórios")
    print('-' * 50)
    print("S - Sair do Sistema")
    
    opcao = input('').upper()
    
    opcoesMenu = {
        '1': "incluirProd()",
        '2': "menuAlterar()",
        '3': "excluirProd()",
        '4': "menuRelatorios()",
        'S': "sys.exit(0)",     # Método exit() da Classe sys que sai da App (Código de Erro 0, sem erro!)
    }

    # Obtem a opção do usuário ou None  p/ opção inválida
    resposta = opcoesMenu.get(opcao)
    if resposta:
        eval( resposta )
    else:
        # clear = Limpa a Tela
        if (os.name.upper() == "POSIX"):
            os.system(command='clear')
        else:
            os.system(command='cls')
        print(f"Opção: '{opcao}' Inválida !!")

while True:
    menu()