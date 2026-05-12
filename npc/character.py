from llm.llm_engine import LLMEngine
from enums.gender import Gender
from npc.memory import Memory
from npc.soul import Soul
import os
import json

class Character:

    def __init__(
        self,
        name: str,
        soul: Soul,
    ):

        self.name = name

        self.soul = soul

        self.memories: list[Memory] = []

        self.llm = LLMEngine()

    def add_memory(self, memory: str):

        self.memories.append(memory)

    def save_memories(self):

        data = [
            {
                "event": memory.event,
                "emotion": memory.emotion,
                "importance": memory.importance,
            }
            for memory in self.memories
        ]
        os.makedirs("data", exist_ok=True)
        with open(f"data/{self.name}_memories.json", "w") as file:
            json.dump(data, file, indent=4)

    def load_memories(self):

        try:

            with open(f"data/{self.name}_memories.json", "r") as file:

                data = json.load(file)

            self.memories = [
                Memory(**memory)
                for memory in data
            ]

        except FileNotFoundError:
            self.memories = []

    def build_system_prompt(self):

        return f"""
        You are an NPC in a medieval world.

        Name: {self.name}

        Gender: {self.soul.gender}

        Personality: {self.soul.personality}

        Goals: {self.soul.goals}

        Beliefs: {self.soul.beliefs}

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