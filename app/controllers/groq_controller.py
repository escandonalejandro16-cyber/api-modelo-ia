from fastapi import APIRouter, HTTPException
from app.models.request_models import GroqRequest
from app.services.groq_service import GroqService

router = APIRouter(prefix="/groq", tags=["Groq"])

service = GroqService()

@router.post("/ask")
def ask_groq(data: GroqRequest):
    try:
        response = service.ask(data.question)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
