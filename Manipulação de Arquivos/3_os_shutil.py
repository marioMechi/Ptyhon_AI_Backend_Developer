import os 
import shutil
from pathlib import Path

ROOT_PATH = Path(__file__).parent

os.mkdir(ROOT_PATH / "novo-diretorio")

arquivo = open(ROOT_PATH / "novo.txt", "w")
arquivo.close()

os.rename(ROOT_PATH / "novo.txt", ROOT_PATH / "alterado.txt")

shutil.move(ROOT_PATH / "alterado.txt", ROOT_PATH / "novo-diretorio"/ "alterado.txt")