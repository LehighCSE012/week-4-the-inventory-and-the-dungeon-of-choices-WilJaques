# Your code goes here
""" adventure game """
import random

def display_player_status(player_health):
    """ Display Player Status """
    print("Your current health:", player_health)

def handle_path_choice(player_health):
    """ Handle Path Choice """
    path = random.choice(["left", "right"])
    if path == "left":
        print("You encounter a friendly gnome who heals you for 10 health points.")
        updated_player_health = player_health + 10
        updated_player_health = min(updated_player_health, 100)
    else:
        print("You fall into a pit and lose 15 health points.")
        updated_player_health = player_health - 15
        if updated_player_health < 0:
            updated_player_health = 0
            print("You are barely alive!")
    return updated_player_health

def player_attack(monster_health):
    """ Player Attack """
    print("You strike the monster for 15 damage!")
    updated_monster_health = monster_health - 15
    return updated_monster_health

def monster_attack(player_health):
    """" Monster Attack """
    crit = random.randint(0,1)
    if crit <= .5:
        print("The monster lands a critical hit for 20 damage!")
        updated_player_health = player_health - 20
    else:
        print("The monster hits you for 10 damage!")
        updated_player_health = player_health - 10
    return updated_player_health

def combat_encounter(player_health, monster_health, has_treasure):
    """" Combat Encounter """
    while player_health > 0 and monster_health > 0:
        monster_health = player_attack(monster_health)
        display_player_status(player_health)
        if monster_health > 0:
            player_health = monster_attack(player_health)
    if player_health <= 0:
        print("Game Over!")
        return False
    elif monster_health <= 0:
        print("You defeated the monster!")
    return has_treasure # boolean

def check_for_treasure(has_treasure):
    """" Check for Treasure """
    if has_treasure:
        print("You found the hidden treasure! You win!")
    else:
        print("The monster did not have the treasure. You continue your journey.")

def acquire_item(inventory, item):
    """ Acquire Item """
    inventory.append(item)
    print(f"You acquired a {item}!")
    return inventory

def display_inventory(inventory):
    """ Display Inventory """
    if len(inventory) == 0:
        print("Your inventory is empty.")
    else:
        print("Your inventory:")
        for i in range(0, len(inventory)):
            print(f"{i+1}. {inventory[i]}")

def enter_dungeon(player_health, inventory, dungeon_rooms):
    """ Enter Dungeon """
    for rooms in dungeon_rooms:
        room_description, item, challenge_type, challenge_outcome = rooms
        print(room_description)

        if item:
            print(f"You found a {item} in the room.")
            inventory = acquire_item(inventory, item)
        if challenge_type == "puzzle":
            print("You encounter a puzzle!")
            skip = input("Do you want to skip or solve the puzzle?")
            if skip == "skip":
                print("You skipped the puzzle.")
            else:
                if random.choice([True, False]):
                    print(challenge_outcome[0])
                    player_health += challenge_outcome[2]
                else:
                    print(challenge_outcome[1])
                    player_health += challenge_outcome[2]

        elif challenge_type == "trap":
            print("You see a potential trap!")
            disarm = input("Do you want to disarm or bypass the trap?")
            if disarm == "disarm":
                if random.choice([True, False]):
                    print(challenge_outcome[0])
                    player_health += challenge_outcome[2] * -1
                else:
                    print(challenge_outcome[1])
                    player_health += challenge_outcome[2]
        elif challenge_type == "none":
            print("There doesn't seem to be a challenge in this room. You move on.")
        if player_health <= 0:
            print("You are barely alive!")

        display_inventory(inventory)
    return player_health, inventory


def main():
    """ Main Function """
    player_health = 100
    monster_health = 70 # Example hardcoded value
    has_treasure = False
    inventory = []
    dungeon_rooms = [
    ("A dusty old library", "key", "puzzle",
     ("You solved the puzzle!", "The puzzle remains unsolved.", -5)),
    ("A narrow passage with a creaky floor", None, "trap",
      ("You skillfully avoid the trap!", "You triggered a trap!", -10)),
    ("A grand hall with a shimmering pool", "healing potion", "none", None)
    ]
    dungeon_rooms.append(("A small room with a locked chest", "treasure", "puzzle",
                    ("You cracked the code!", "The chest remains stubbornly locked.", -5)))

    has_treasure = random.choice([True, False]) # Randomly assign treasure

    player_health = handle_path_choice(player_health)

    treasure_obtained_in_combat = combat_encounter(player_health, monster_health, has_treasure)

    check_for_treasure(treasure_obtained_in_combat) # Or has_treasure, depending on logic

    player_health, inventory = enter_dungeon(player_health, inventory, dungeon_rooms)
    print(player_health)

if __name__ == "__main__":
    main()
