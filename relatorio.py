import sqlite3 as sql
from stringsSql import *

conn=sql.connect("Produtos.db")
cur=conn.cursor()
cur.execute(comandosSql[4])
lista=cur.fetchall()
print("CÓDIGO\tDESCRIÇÃO\tPREÇO\tQT\tPESO\tDATA")
print("-" * 50)
for linha in lista:
  codigo, descricao, preco, qt, peso, data = linha
  print(f"{codigo}\t{descricao}\t{preco}\t{qt}\t{peso}\t{data}")
