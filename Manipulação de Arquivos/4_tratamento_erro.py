from pathlib import Path

#try:
#    arquivo = open("meu_arquivo.py")
#except FileNotFoundError as exec:
#    print("Arquivo não encontrado")
#    print(exec)

ROOT_PATH = Path(__file__).parent

try:
    arquivo = open(ROOT_PATH / "novo-diretorio")
except IsADirectoryError as exec:
    print(f"Não foi possível abrir o arquivo: {exec}")
except IOError as exec:
    print(f"Não foi possível abrir o arquivo: {exec}")
except Exception as exec:
    print(f"Não foi possível abrir o arquivo: {exec}")