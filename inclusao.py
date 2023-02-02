import sqlite3 as sql
from stringsSql import comandosSql

conn=sql.connect("Produtos.db")
cur=conn.cursor()
        
while True:
    descricao   = input("Digite a Descrição do produto: ")
    preco       = float( input("Digite a Preço: ") )
    quant       = int( input("Digite a Quantidade: ") )
    massa       = float( input("Digie o PESO: ") )
    vecto       = input("Digite a Data: (AAAAMMDD): ")
    cur.execute( comandosSql[3], (descricao, preco, quant, massa, vecto) )
    # Salvar os dados no Banco
    conn.commit()
    opcao = input("Continuar (S/N)?").upper()
    if opcao!='S':
        break
#Fim do While