from groq import Groq
from app.core.config import GROQ_API_KEY
from app.memory.conversation_memory import ConversationMemory
from app.agents.ventas_agent import VENTAS_SYSTEM_PROMPT


class GroqService:
    def __init__(self):
        self.client = Groq(api_key=GROQ_API_KEY)
        self.memory = ConversationMemory(max_turns=20)

    def ask_ventas(self, user_id: str, question: str) -> str:
        agent = "ventas"

        # Recuperar memoria
        history = self.memory.get_context(user_id, agent)

        messages = [
            {"role": "system", "content": VENTAS_SYSTEM_PROMPT},
            *history,
            {"role": "user", "content": question}
        ]

        completion = self.client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=messages,
            temperature=0.4,
            max_tokens=250
        )

        answer = completion.choices[0].message.content

        # Guardar memoria
        self.memory.add_message(user_id, agent, "user", question)
        self.memory.add_message(user_id, agent, "assistant", answer)

        return answer
