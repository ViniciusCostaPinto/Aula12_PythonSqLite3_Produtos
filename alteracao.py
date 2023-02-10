from conexao import conectar
from stringsSql import *

def validarCodigo(chaveConsultaSql):
    conn, cur = conectar("Produtos.db")
    codigo = int( input("Informe o Código do Produto") )
    cur.execute( comandosSql.get(chaveConsultaSql), (codigo,) )
    registro = cur.fetchone()
    
    return (registro)
    
    
def alterarDesc():
    codigoExiste = validarCodigo(1)
    if codigoExiste:
        novaDescricao = input(f"Informe a Nova descrição do produto {codigoExiste[1]}: ")
        conn, cur = conectar("Produtos.db")
        cur.execute(comandosSql.get(5), (novaDescricao, codigoExiste[0]))
        conn.commit()
        return True
    else:
        print("Código do Produto não Cadastrado!!")
        return False

        
def alterarPreco():
    pass

def alterarQt():
    pass

def alterarPeso():
    pass

def alterarVecto():
    pass