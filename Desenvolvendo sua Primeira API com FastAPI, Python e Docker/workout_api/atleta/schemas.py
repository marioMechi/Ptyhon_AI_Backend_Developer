from pydantic import  PositiveFloat, Field
from typing import Annotated
from workout_api.contrib.schemas import BaseSchema

class Atleta(BaseSchema):
    nome: Annotated[str, Field(description="Nome do Atleta", example="João", max_length=50)]
    cpf: Annotated[str, Field(description="CPF do Atleta", example="000.000.000-00", max_length=11)]
    idade: Annotated[int, Field(description="Idade do Atleta", example="30")]
    peso: Annotated[PositiveFloat, Field(description="Peso do Atleta", example="80")]
    altura: Annotated[PositiveFloat, Field(description="Altura do Atleta", example="1.80")]
    sexo: Annotated[str, Field(description="Sexo do Atleta", example="M", max_length=1)]
