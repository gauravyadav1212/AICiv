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