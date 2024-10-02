import sqlite3

# Conectar ao banco de dados
conn = sqlite3.connect("formulario.db")

# Criar um cursor
cursor = conn.cursor()

# Criar a tabela
cursor.execute("""
    CREATE TABLE formulario (
        id INTEGER PRIMARY KEY,
        nome TEXT NOT NULL,
        email TEXT NOT NULL,
        telefone TEXT NOT NULL,
        endereco TEXT NOT NULL,
        cidade TEXT NOT NULL,
        estado TEXT NOT NULL,
        cep TEXT NOT NULL
    );
""")

# Fechar a conexão com o banco de dados
conn.close()
