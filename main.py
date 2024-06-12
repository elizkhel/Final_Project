import random
from character import CharacterPicker
from history import save_attack_history, display_attack_history


def choose_character(char_map):
    print("Available characters:")
    for i, character_name in enumerate(list(char_map.keys())): # i gamoviyeneb index, character_name ro mivwvde dictionary-s key-ebs.
        print(f"{i + 1}. {character_name}")

    while True:
        try:
            choice = int(input("Choose your character by number: ")) - 1
            if 0 <= choice < len(char_map):
                return char_map.pop(list(char_map.keys())[choice])() # archeuli class (character) gamodzaxeba 
            else:
                print("Invalid choice, please try again.")
        except ValueError:
            print("Invalid input, please enter a number.")
        # except Exception as e:
        #     print(f"An unexpected error occurred: {e}")


# tamashi logikis gawera 
def play_game(player1, player2):
    print(f"{player1.name} vs {player2.name}!")
    characters = [player1, player2]
    current_turn = 0

    while player1.is_alive() and player2.is_alive():
        current_player = characters[current_turn] # monacvleoba 2 motamashes shoris
        opponent = characters[1 - current_turn] # player 1 and 2 list [0,1]

        try:
            command = input(f"{current_player.name}'s turn (attack, special, history, quit): ").strip().lower()
            if command == "attack": # attack funqciis gamodzaxeba 
                current_player.attack(opponent)
                if not opponent.is_alive():
                    break
            elif command == "special": # speacial_abolity funqciis gamodzaxeba 
                current_player.use_special_ability(opponent)
                if not opponent.is_alive():
                    break
            elif command == "history": # shua tamshis tu mounda history-s naxva 
                display_attack_history(characters)
                continue  # monacvleobis chanawerebis amogeba   history-shi
            elif command == "quit": # tamashidan exit 
                print("Thanks for playing!")
                display_attack_history(characters)
                save_attack_history(characters, "attack_history.csv")
                return
            else:
                print("Unknown command. Type 'attack', 'special', 'history', or 'quit'.")
                continue

            current_turn = 1 - current_turn
        except Exception as e:
            print(f"An error occurred during the turn: {e}")

    if player1.is_alive():
        print(f"{player1.name} wins!")
    else:
        print(f"{player2.name} wins!")
    
    try:
        display_history = input("Display attack history? (yes/no): ").strip().lower()
        if display_history == "yes":
            display_attack_history(characters)
    except Exception as e:
        print(f"An error occurred while displaying attack history: {e}")
    
    try:
        save_history = input("Save attack history? (yes/no): ").strip().lower()
        if save_history == "yes":
            save_attack_history(characters, "attack_history.csv")
    except Exception as e:
        print(f"An error occurred while saving attack history: {e}")


def main():
    print("Welcome to the fighting game!")
    char_picker = CharacterPicker()
    try:
        player1 = choose_character(char_picker.char_map)
        player2 = choose_character(char_picker.char_map)
        play_game(player1, player2)
    except Exception as e:
        print(f"An error occurred in the game: {e}")
        

if __name__ == "__main__":
    main()