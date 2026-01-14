from pydantic import BaseModel

# Para preguntas generales
class GroqRequest(BaseModel):
    question: str

# Para el agente de ventas
class VentasRequest(BaseModel):
    user_id: str  # Para identificar la conversación
    question: str
