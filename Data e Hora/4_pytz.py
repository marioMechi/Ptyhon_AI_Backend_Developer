#pip install pytz
#python -m venv .env
#source .env/bin/activate

import pytz
from datetime import datetime

data = datetime.now(pytz.timezone('Europe/Oslo')) 
data2 = datetime.now(pytz.timezone('America/Sao_Paulo'))

print(data, data2)