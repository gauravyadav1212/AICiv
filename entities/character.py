from llm.llm_engine import LLMEngine
from enum import Enum

class Gender(Enum):
    MALE = "male"
    FEMALE = "female"


class NPC:

    def __init__(
        self,
        name: str,
        personality: list[str],
        goals: list[str],
        gender: Gender
    ):

        self.name = name
        self.personality = personality
        self.goals = goals
        self.gender = gender

        self.memories = []
        self.relationships = {}

        self.llm = LLMEngine()

    def add_memory(self, memory: str):

        self.memories.append(memory)

    def build_system_prompt(self):

        return f"""
        You are an NPC in a medieval world.

        Name: {self.name}

        Gender: {self.gender}

        Personality:
        {", ".join(self.personality)}

        Goals:
        {", ".join(self.goals)}

        Recent Memories:
        {self.memories[-5:]}

        Always return valid JSON.

        Format:
        {{
            "thought": "...",
            "action": "...",
            "target": "..."
        }}
        """
    
    def think(self, situation: str):

        result = self.llm.generate(
            system_prompt=self.build_system_prompt(),
            user_prompt=situation
        )

        return result