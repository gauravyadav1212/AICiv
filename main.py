from entities.character import NPC
from entities.character import Gender

edric = NPC(
    name="Edric",
    personality=["forgiving", "lovable", "hardworker"],
    goals=["gain power", "become rich"],
    gender=Gender.MALE
)

edric.add_memory("Rowan insulted me in the tavern.")

response = edric.think(
    "You see Rowan entering the tavern again."
)

print(response)