from utils.printer import print_response
from npc.character import Character
from world.location import Location

class World:

    def __init__(self):

        self.characters: list[Character] = []

        self.locations: list[Location] = []

    def add_character(self, character):

        self.characters.append(character)

    def add_location(self, location):

        self.locations.append(location)

    def get_characters_in_location(
        self,
        location
    ):

        return [
            character
            for character in self.characters
            if character.location == location
        ]
    
    def broadcast_event(
        self,
        event,
        location=None
    ):

        listeners = self.characters

        if location:

            listeners = [
                character
                for character in self.characters
                if character.location == location
            ]

        for character in listeners:

            reaction = character.observe(event)

            print_response(character, reaction)

    def run(self):

        for character in self.characters:

            reaction = character.think("What would you do now?")

            print_response(character, reaction)

    def describe(self):

        print("Welcome to the world!")
        print("Characters: ")
        for character in self.characters:
            print(character.name)
            print(f"  Location: {character.location.name}") 
            print(f"  Memories: {len(character.memories)}")
            print(f"  Soul: {', '.join(character.soul.personality)}")
            print("\n")

        print("Locations: ")
        for location in self.locations:
            print(location.name)
            print(f"  Description: {location.description}")
            print(f"  Type: {location.location_type}")
            print(f"  Social Class: {location.social_class}")
            print(f"  Danger Level: {location.danger_level}")
            print("\n")