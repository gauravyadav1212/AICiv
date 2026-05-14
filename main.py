from npc.character import Character
from enums.gender import Gender
from enums.roles import Role
from npc.soul import Soul
from npc.memory import Memory
from npc.conversation_manager import run_conversation
from world.world import World
from world.location import Location
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


# Locations

traven = Location(
    name="traven", 
    description="An ancient structure made of stone and decorated with rich plants and a pleasing aroma",
    location_type="social place",
    social_class="commoner",
    danger_level=0.2
    )

traven.add_lore("This was the first major building in village, made centuries ago and has belonged to the same family since its creation")

traven.add_rumor("This served as the hiding place of king aflred during the black wars")

# Characters

edric = Character(
    name="Edric",
    soul=edric_soul,
    spawn_location=traven
)

rowan = Character(
    name="rowan",
    soul=rowan_soul,
    spawn_location=traven
)

mira = Character(
    name="mira",
    soul=mira_soul,
    spawn_location=traven
)

roderick = Character(
    name="roderick",
    soul=roderick_soul,
    spawn_location=traven
)


traven.owner = mira
characters = [edric, rowan, mira, roderick]
locations = [traven]

world = World()

for location in locations:
    world.add_location(location)

for character in characters:
    world.add_character(character)

world.describe()

initial_event = input(
    "\nPlease enter initial Event: "
)

world.broadcast_event(initial_event)

while (True):

    command = input(
        "\nPress ENTER to continue or type 'exit': "
    )

    if command.lower() == "exit":
        break

    world.run()