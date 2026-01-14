from fastapi import FastAPI
from app.controllers.groq_controller import router as groq_router

app = FastAPI(
    title="Groq API MVC",
    version="1.0.0"
)

app.include_router(groq_router)

@app.get("/")
def health():
    return {"status": "ok"}
