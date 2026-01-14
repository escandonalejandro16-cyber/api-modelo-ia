import os
from fastapi import FastAPI
from app.controllers.groq_controller import router as groq_router
import uvicorn

app = FastAPI(
    title="Groq API MVC-2",
    version="1.0.0"
)

# Registrar router
app.include_router(groq_router)

# Health check
@app.get("/")
def health():
    return {"status": "ok"}

# Solo si ejecutas este archivo directamente
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))  # Render asigna este puerto automáticamente
    uvicorn.run("main:app", host="0.0.0.0", port=port, log_level="info")
