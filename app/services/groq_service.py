from groq import Groq
from app.core.config import GROQ_API_KEY

class GroqService:

    def __init__(self):
        self.client = Groq(api_key=GROQ_API_KEY)

    def ask(self, question: str) -> str:
        completion = self.client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "system", "content": "Eres un asistente experto en sistemas e IA."},
                {"role": "user", "content": question}
            ],
            temperature=0.3,
            max_tokens=200
        )

        if not completion.choices:
            raise ValueError("Respuesta vacía del modelo")

        return completion.choices[0].message.content
