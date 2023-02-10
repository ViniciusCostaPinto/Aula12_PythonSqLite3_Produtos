# Importando os módulos do S.O.(Sistema Operacional)
import os

# importações necessárias para carregar os módulos da Aplicação:
from alteracao import alterarDesc, alterarPreco, alterarQt, alterarPeso, alterarVecto

# Função do Menu principal
def menuAlterar():
    opcao = None
    while (opcao != 'S'):
        print("Alteração de Produtos:")
        print('=' * 50)
        print("1 - Alteração da Descrição")
        print("2 - Alteração de Preço")
        print("3 - Alteração de Quantidade")
        print("4 - Alteração de Peso")
        print("5 - Alteração de Vencimento")
        print('-' * 50)
        print("S - Sair para o Menu Principal")
        
        opcao = input().upper()
        
        opcoesMenu = {
            '1': "alterarDesc()",
            '2': "alterarPreco()",
            '3': "alterarQt()",
            '4': "alterarPeso()",
            '5': "alterarVecto()",
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