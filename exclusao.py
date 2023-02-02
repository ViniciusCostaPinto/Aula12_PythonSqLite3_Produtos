import sqlite3 as sql
from stringsSql import comandosSql

conn=sql.connect("Produtos.db")
cur=conn.cursor()
while True:
    codigo=int( input("Código do Produto: ") )
    
    cur.execute( comandosSql[1],  (codigo,) )
    respostaConsulta = cur.fetchone()    
    codigo, descricao = respostaConsulta if (respostaConsulta != None) else (None, None)

    if codigo != None:    # ou poderia usar: if len(listaCodigo) == 1:
        confirmaExclusao = input( f"Confirma Exclusão Produto: {descricao} (S/N):" ).upper()
        if confirmaExclusao == 'S':
            cur.execute(comandosSql[2], (codigo,))
            conn.commit()
    else:
        print("Código Inválido!", end="\n\n")
    
    excluirMais = input("Continuar com exclusões? (S/N)").upper()
    if excluirMais != 'S':
        break
        