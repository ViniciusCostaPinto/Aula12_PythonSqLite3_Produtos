comandosSql = {
    0 : """
            CREATE TABLE IF NOT EXISTS Produtos ( 
            codigo INTEGER PRIMARY KEY AUTOINCREMENT,
            descricao TEXT,
            preco REAL,
            qt INTEGER,
            peso REAL,
            vencimento TEXT )
        """,
    1 : "SELECT codigo, descricao FROM Produtos WHERE codigo = ?",
    2 : "DELETE FROM Produtos WHERE codigo = ?",
    3 : "INSERT INTO produtos ( descricao, preco, qt, peso, vencimento) VALUES ( ?, ?, ?, ?, ?)",
    4 : "SELECT * FROM Produtos"
}
