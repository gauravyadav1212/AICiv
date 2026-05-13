from npc.character import Character
import json

def print_response(character: Character, response: json):

    print(f"{character.name}")
    print("-" * 30)

    print(f"Thought: {response['thought']}")

    if "emotion" in response:
        print(f"Emotion: {response['emotion']}")

    if "action" in response:
        print(f"Action: {response['action']}")

    if "target" in response:
        print(f"Target: {response['target']}")

    print("\n")