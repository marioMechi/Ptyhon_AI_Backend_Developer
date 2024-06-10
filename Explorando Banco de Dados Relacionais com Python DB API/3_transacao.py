import sqlite3
from pathlib import Path

ROOT_PATH = Path (__file__).parent
conexao = sqlite3.connect(ROOT_PATH /'meu_bando.sqlite')
cursor = conexao.cursor()
cursor.row_factory = sqlite3.Row

# with conexao = sqlite3.connect(ROOT_PATH /'meu_bando.sqlite') as conexao

try:
    cursor.execute("INSERT INTO clientes (nome, email) VALUES (?,?)", ('teste4','teste4@gmail.com'))
    cursor.execute("INSERT INTO clientes (id, nome, email) VALUES (?,?,?)", (2, 'teste5','teste5@gmail.com'))
    conexao.commit()
except Exception as exc:
    print(f"Ops, erro ocorreu: {exc}")
    conexao.rollback()
#finally:
#    conexao.commit()