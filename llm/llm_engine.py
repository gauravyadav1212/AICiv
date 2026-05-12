from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, SystemMessage
import json


class LLMEngine:
    def __init__(
        self,
        model: str = "mistral:latest",
        temperature: float = 0.7,
    ):

        self.llm = ChatOllama(
            model=model,
            temperature=temperature,
            format="json",
        )

    def generate(
        self,
        system_prompt: str,
        user_prompt: str,
    ) -> dict:

        messages = [
            SystemMessage(content=system_prompt),
            HumanMessage(content=user_prompt),
        ]

        response = self.llm.invoke(messages)

        try:
            return json.loads(response.content)

        except Exception as e:
            return {
                "status": "error",
                "message": str(e),
                "raw_output": response.content,
            }