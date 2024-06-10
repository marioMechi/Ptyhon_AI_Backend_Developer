import sqlite3
from pathlib import Path

ROOT_PATH = Path (__file__).parent
conexao = sqlite3.connect(ROOT_PATH /'meu_bando.sqlite')
cursor = conexao.cursor()
cursor.row_factory = sqlite3.Row

id_cliente = input("Informe id do cliente:")
cursor.execute("SELECT * FROM clientes WHERE id=?",(id_cliente, ))

clientes = cursor.fetchall()
for cliente in clientes:
    print(dict(cliente))
    
# Forma Incorreta
# 1 OR 1=1
#cursor.execute(f"SELECT * FROM clientes WHERE id={id_cliente}")