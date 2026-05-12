from npc.character import Character
from enums.gender import Gender
from enums.roles import Role
from npc.soul import Soul
from npc.memory import Memory

edric_soul = Soul(
    personality=["greedy", "paranoid"],
    goals=["gain power"],
    fears=["public humiliation"],
    beliefs=["people are selfish"],
    gender=Gender.MALE,
    role=Role.EARL
)

edric = Character(
    name="Edric",
    soul=edric_soul
)


edric.add_memory(
    Memory(
        event="Rowan insulted me publicly.",
        emotion="anger",
        importance=0.9
    )
)

edric.save_memories()

result = edric.think("You meet Rowan again in traven")
print(result)
