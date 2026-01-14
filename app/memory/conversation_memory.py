from typing import List, Dict

class ConversationMemory:
    """
    Memoria por usuario y por agente.
    Limita a `max_turns` mensajes por conversación.
    """
    def __init__(self, max_turns: int = 20):
        self.memory: Dict[str, List[Dict[str, str]]] = {}
        self.max_turns = max_turns

    def _get_key(self, user_id: str, agent: str) -> str:
        return f"{user_id}:{agent}"

    def add_message(self, user_id: str, agent: str, role: str, content: str):
        """
        Agrega un mensaje a la memoria
        role: 'user' o 'assistant'
        """
        key = self._get_key(user_id, agent)
        if key not in self.memory:
            self.memory[key] = []

        self.memory[key].append({"role": role, "content": content})

        # Limitar memoria a max_turns
        if len(self.memory[key]) > self.max_turns:
            self.memory[key] = self.memory[key][-self.max_turns:]

    def get_context(self, user_id: str, agent: str) -> List[Dict[str, str]]:
        """
        Retorna la memoria completa del usuario y agente
        """
        key = self._get_key(user_id, agent)
        return self.memory.get(key, [])
