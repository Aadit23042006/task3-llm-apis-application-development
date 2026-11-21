from typing import List, Dict

Message = Dict[str, str]

class Conversation:
    def __init__(self, system_prompt: str = "You are a helpful, concise assistant."):
        self.system_prompt = system_prompt.strip() or "You are a helpful assistant."
        self.messages: List[Message] = []

    def api_messages(self) -> List[Message]:
        return [{"role": "system", "content": self.system_prompt}, *self.messages]

    def add_user(self, content: str) -> None:
        content = content.strip()
        if content:
            self.messages.append({"role": "user", "content": content})

    def add_assistant(self, content: str) -> None:
        self.messages.append({"role": "assistant", "content": content})

    def clear(self) -> None:
        self.messages.clear()

    def replace_system_prompt(self, prompt: str) -> None:
        self.system_prompt = prompt.strip() or "You are a helpful assistant."
