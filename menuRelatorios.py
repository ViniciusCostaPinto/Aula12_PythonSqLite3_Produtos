import os
from relatorios import *

def menuRelatorios():
    opcao = None
    while (opcao != 'S'):
        print("Relatórios:")
        print('=' * 50)
        print("1 - Todos os Produtos")
        print("2 - Lista Produto por Código")
        print("3 - ")
        print("4 - ")
        print("5 - ")
        print('-' * 50)
        print("S - Sair para o Menu Principal")
        
        opcao = input().upper()
        
        opcoesMenu = {
            '1': "listarTodos()",
            '2': "listarPorCodigo()",
            '3': "()",
            '4': "()",
            '5': "()",
            'S': "()"
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