# Importa a Biblioteca do Banco de Dados SQLite 3
import sqlite3 as sq
# Importa o Dicionário das Strings SQL
import stringsSql

# Cria uma 'Conexão' com o banco de dados físico
conn = sq.connect("Produtos.db")

# O Cursor é um MiddleWare entre a Consulta
#  SQL e o Banco de Dados.
cur = conn.cursor()

resposta = cur.execute(stringsSql.stringsSql[0])

if resposta:
    print("Banco de Dados Produtos, criado com sucesso!")
else:
    print("Erro na criação do Banco de Dados Produtos!!")
