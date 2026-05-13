from npc.memory import Memory
from npc.character import Character
from utils.printer import print_response

def broadcast_event(characters: list[Character], event):

    for character in characters:

        reaction = character.observe(event)

        print_response(character, reaction)