from utils.printer import print_response

class World:

    def __init__(self):

        self.characters = []

        self.locations = []

    def add_character(self, character):

        self.characters.append(character)

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