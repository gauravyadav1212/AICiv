from __future__ import annotations
from llm.llm_engine import LLMEngine
from enums.gender import Gender
from npc.memory import Memory
from npc.soul import Soul
from typing import TYPE_CHECKING
import os
import json

if TYPE_CHECKING:
    from world.location import Location

class Character:

    def __init__(
        self,
        name: str,
        soul: Soul,
        spawn_location: Location | None = None
    ):

        self.name = name

        self.soul = soul

        self.memories: list[Memory] = []

        self.llm = LLMEngine()

        self.location = spawn_location

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
        You are a human in a medieval world.

        Name: {self.name}

        Gender: {self.soul.gender}

        Personality: {self.soul.personality}

        Goals: {self.soul.goals}

        Beliefs: {self.soul.beliefs}

        Role/Job: {self.soul.role}

        Your current location: {self.location.name}

        Recent Memories:
        {self.memories[-5:]}

        Always return valid JSON.

        Format:
        {{
            "thought": "...",
            "action": "...",
            "target": "..."
        }}

        Your actions should realistically match:
        - your role
        - your resources
        - your social position
        - your personality

        Do not behave like a spymaster unless your role supports it.
        """
    
    def build_observe_prompt(self):

        return f"""
        You are an NPC in a medieval world.

        Name: {self.name}

        Gender: {self.soul.gender}

        Personality: {self.soul.personality}

        Goals: {self.soul.goals}

        Beliefs: {self.soul.beliefs}

        Role/Job: {self.soul.role}

        Your current location: {self.location.name}

        Recent Memories:
        {self.memories[-5:]}

        You are observing an event.

        Respond naturally.

        DO NOT take action.
        DO NOT make plans.
        DO NOT escalate situations.

        Return valid JSON:

        {{
            "thought": "...",
            "emotion": "...",
            "importance": 0.0
        }}
        """
    
    def observe(self, event: str):

        result = self.llm.generate(
            system_prompt=self.build_observe_prompt(),
            user_prompt=event
        )

        memory = Memory(
            event=event,
            emotion=result["emotion"],
            importance=result["importance"]
        )

        self.add_memory(memory)

        return result

    def think(self, situation: str):

        result = self.llm.generate(
            system_prompt=self.build_system_prompt(),
            user_prompt=situation
        )

        return result
    
    def move_to(self, location: Location):

        self.location = location