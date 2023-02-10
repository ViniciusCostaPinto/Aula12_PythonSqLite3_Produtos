import sqlite3 

def conectar(bd):
    conexao=sqlite3.connect(bd)
    cursor=conexao.cursor()
    return (conexao, cursor)