from npc.character import Character
from utils.printer import print_response
def run_conversation(characters: list[Character], initial_event, rounds=2):

    history = [f"Event: {initial_event}"]

    for _ in range(rounds):

        for character in characters:

            context = "\n".join(history)

            response = character.think(context)
            print_response(character, response)
            
            action = response.get("action", "")

            history.append(
                f"{character.name}: {action}"
            )

    return history