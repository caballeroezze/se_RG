# Aquí irá la API con FastAPI

from fastapi import FastAPI
from pydantic import BaseModel
from engine import inferir_recomendaciones

app = FastAPI()

# Modelo de entrada (lo que espera recibir la API)
class Perfil(BaseModel):
    perfil_usuario: str

# Endpoint POST para recibir el perfil y devolver recomendaciones
@app.post("/recommend")
def recommend(perfil: Perfil):
    resultado = inferir_recomendaciones(perfil.perfil_usuario)
    return resultado
