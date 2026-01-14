from pydantic import BaseModel

class GroqRequest(BaseModel):
    question: str
