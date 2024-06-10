import csv
from pathlib import Path
ROOTH_PATH = Path(__file__).parent
COLUNA_ID = 0
COLUNA_NOME =  1
try:
    with open(ROOTH_PATH / "usuarios.csv", "w", newline = '', encoding= "utf-8")as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow(['id', 'nome'])
        escritor.writerow(['1', 'Maria'])
        escritor.writerow(['2', 'João'])
except IOError as exc:
    print(f"Erro ao abrir ao arquivo {exc}")

try:
    with open(ROOTH_PATH / "usuarios.csv", "r", newline = '', encoding= "utf-8")as arquivo:
        leitor = csv.reader(arquivo)
        for idx, row in enumerate(leitor):
            if idx == 0:
                continue
            print(f"ID: {row[COLUNA_ID]}")
            print(f"NOME: {row[COLUNA_NOME]}")
except IOError as exc:
    print(f"Erro ao abrir ao arquivo {exc}")

try:
    with open("name.csv", newline = '', encoding= "utf-8")as csvfile:
        leitor = csv.DictReader(csvfile)
        print(csv.reader.fieldnames)
        #for row in leitor:
        #    print(row)
except IOError as exc:
    print(f"Erro ao abrir ao arquivo {exc}")