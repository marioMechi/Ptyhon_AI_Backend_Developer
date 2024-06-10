from pathlib import Path

ROOT_PATH = Path(__file__).parent

try:
    with open(ROOT_PATH / "1lorem.txt", "r") as arquivo:
        print(arquivo.read())
except IOError:
    print("Erro ao abrir arquivo")

try:
    with open(ROOT_PATH / "arquivo-utf-8.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write("Aprendendo a manipular arquivos utilixando Phyton")
except IOError as exc:
    print(f"Erro ao abrir arquivo: {exc}")

try:
    with open(ROOT_PATH / "arquivo-utf-8.txt", "w", encoding="ascii") as arquivo:
        arquivo.write("Aprendendo a manipular arquivos utilixando Phyton")
except IOError as exc:
    print(f"Erro ao abrir arquivo: {exc}")

