from npc.character import Character
from enums.gender import Gender
from enums.roles import Role
from npc.soul import Soul
from npc.memory import Memory
from world.event_manager import broadcast_event
from npc.conversation_manager import run_conversation

# SOULS

edric_soul = Soul(
    personality=["greedy", "paranoid"],
    goals=["gain power"],
    fears=["public humiliation"],
    beliefs=["people are selfish"],
    gender=Gender.MALE,
    role=Role.EARL
)

rowan_soul = Soul(
    personality=["honorable", "hot-headed", "proud"],
    goals=["protect reputation"],
    fears=["cowardice"],
    beliefs=["strength earns respect"],
    gender=Gender.MALE,
    role=Role.KNIGHT
)

mira_soul = Soul(
    personality=["observant", "pragmatic"],
    goals=["protect livelihood"],
    fears=["violence"],
    beliefs=["everyone has secrets"],
    gender=Gender.FEMALE,
    role=Role.TAVERN_KEEPER
)

roderick_soul = Soul(
    personality=["disciplined", "pragmatic", "stern"],
    goals=["maintain order"],
    fears=["civil unrest"],
    beliefs=["stability requires strength"],
    gender=Gender.MALE,
    role=Role.MARSHAL
)


# Characters

edric = Character(
    name="Edric",
    soul=edric_soul
)

rowam = Character(
    name="rowan",
    soul=rowan_soul
)

mira = Character(
    name="mira",
    soul=mira_soul
)

roderick = Character(
    name="roderick",
    soul=roderick_soul
)



characters = [
    edric,
    rowam,
    mira,
    roderick
]

print("Initial Event: \n\n")


broadcast_event(
    characters,
    "Rowan publicly insults Edric in the tavern."
)

print("Conversations: \n\n")

run_conversation(
    characters,
    "Rowan publicly insults Edric in the tavern.",
    rounds=3
)