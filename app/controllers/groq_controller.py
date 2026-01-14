from fastapi import APIRouter, HTTPException
from app.services.groq_service import GroqService
from app.models.request_models import VentasRequest

router = APIRouter(prefix="/ventas", tags=["Agente Ventas"])

service = GroqService()


@router.post("/chat")
def ventas_chat(data: VentasRequest):
    try:
        answer = service.ask_ventas(
            user_id=data.user_id,
            question=data.question
        )
        return {"answer": answer}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
