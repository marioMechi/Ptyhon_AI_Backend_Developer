from typing import Annotated

from pydantic import Field
from workout_api.contrib.schemas import BaseSchema

class CentroTreinamento(BaseSchema):
    nome: Annotated[str, Field(description="Nome do centro de treinamento", example="Cidade do Galo", max_length=20)]
    endereco: Annotated[str, Field(description="Endereço do centro de treinamento", example="Rodovia MG 424", max_length=60)]
    proprietario: Annotated[str, Field(description="Proprietário do centro de treinamento", example="4 R's", max_length=30)]