import sqlite3 as sql
from stringsSql import *
from conexao import conectar

def listarTodos():
  _, cur = conectar("Produtos.db")
  cur.execute(comandosSql[4])
  lista=cur.fetchall()
  print("CÓDIGO\tDESCRIÇÃO\tPREÇO\tQT\tPESO\tDATA")
  print("-" * 50)
  for linha in lista:
    codigo, descricao, preco, qt, peso, data = linha
    print(f"{codigo}\t{descricao}\t{preco}\t{qt}\t{peso}\t{data}")
  input("Pressione qq tecla p/continuar...")
