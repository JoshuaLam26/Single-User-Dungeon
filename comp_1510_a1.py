"""Assignment 1 SUD"""

# Joshua Lam
# A00959199
# November 9, 2018

import json
import random


# Functions that start the game
def get_user_name():
    """Ask the user for their name.

    PARAM: none
    PRECONDITION: none
    POSTCONDITION: Transform the user input into title case and strip the whitespace
    RETURN: A stripped title case username of type string
    """
    print("What's your name (type your previous name to load saved data)\n"
          "(If you died in your last game, new game will be created)\n"
          "(You may only use letters in your name):")
    username = get_user_input()
    username = username.strip()
    username = username.title()
    return username


def get_user_input():
    """Ask the user for their name.

    Their input may only contain spaces, lower case letters, and upper case letters.
    If it contains any other characters, the function will recursively call itself until a valid input is given.
    PARAM: none
    PRECONDITION: none
    POSTCONDITION: asks user for their name
    RETURN: a username of type string
    """
    valid_inputs = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                    'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
                    'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ' ']
    username = input()
    if len(username) < 1:
        print("Name must be at least one letter. Please enter another name:")
        username = get_user_input()
    for letter in username:
        if letter not in valid_inputs:
            print("Username can only contain letters. Please enter another name:")
            username = get_user_input()
    return username


def start_game():
    """Create a new user game file or open saved user game file

    A user game file is a .json file that holds the username(string), hp(int), row_loc(int), col_loc(int), and sud_map.
    sud_map is a list of list of dictionaries where the first list represents the map rows, the nested list represents
    the map columns, and the dictionaries represent each map cell.
    PARAM: none
    PRECONDITION: none
    POSTCONDITION: Create or open a .json file that is a well formed game file
    RETURN: the users .json game file information of type dictionary
    """
    # get the users name
    username = get_user_name()
    filename = username + ".json"
    max_hp = 10
    # Try and open the json file.
    try:
        with open(filename):
            print("Welcome back " + username + ", loading your saved game now!")
            print_scenario()
    # Create a new json file if it is not in the project.
    except FileNotFoundError:
        print("Welcome " + username + ", creating your account now!")
        with open(filename, "w") as file_object:
            json.dump({"username": username,
                       "hp": max_hp,
                       "row_loc": 0,
                       "col_loc": 0,
                       "sud_map": create_map()}, file_object)
            print_scenario()
    # Return the json file's data
    with open(filename) as file_object:
        return json.load(file_object)


def create_map():
    """Create a 4 by 4 game map.

    A well formed map is a list of 4 lists of 4 dictionaries.
    The first list refers to the map rows. The nested list refers to the map columns.
    The dictionaries refer to the information of each cell. Each dictionary contains an appearance and a description.
    The appearance of a cell will be [ ] if empty and [X] if the character is inside it.
    PARAM: none
    PRECONDITION: none
    POSTCONDITION: create a map with the characters appearance in cell [0,0]
    RETURN: list of 4 list of 4 dictionaries, a game map
    """
    map_size = 4
    sud_map = [row for row in range(map_size)]
    for rows in sud_map:
        sud_map[rows] = [column for column in range(map_size)]
        for col in range(map_size):
            sud_map[rows][col] = {"appearance": "[ ]", "description": "This block has no description"}
    sud_map[0][0]["appearance"] = "[X]"
    load_descriptions(sud_map)
    return sud_map


def load_descriptions(sud_map):
    """Change the description of each map cell.

    A well formed map is a list of 4 lists of 4 dictionaries.
    The first list refers to the map rows. The nested list refers to the map columns.
    The dictionaries refer to the information of each cell. Each dictionary contains an appearance and a description.
    The appearance of a cell will be [ ] if empty and [X] if the character is inside it.
    PARAM: sud_map, a list of list of dictionaries
    PRECONDITION: sud_map must be a well formed map.
    POSTCONDITION: All of the descriptions of each cell in sud_map are changed
    RETURN: none
    """
    with open("DESCRIPTIONS.json", "r") as description_file_object:
        description_dictionary = json.load(description_file_object)
        for row in range(4):
            for col in range(4):
                description_key = str(row) + str(col)
                sud_map[row][col]["description"] = description_dictionary[description_key]


# Functions that print the game for players to see
def print_scenario():
    """Print the scenario of the game.

    PARAM: none
    PRECONDITION: none
    POSTCONDITION: print the game scenario
    RETURN: string, the came scenario
    """
    print("""
          _                         _                         _     
         | |                       (_)                       | |    
         | |_   _ _ __ __ _ ___ ___ _  ___   _ __   __ _ _ __| | __ 
     _   | | | | | '__/ _` / __/ __| |/ __| | '_ \ / _` | '__| |/ / 
    | |__| | |_| | | | (_| \__ \__ \ | (__  | |_) | (_| | |  |   <  
     \____/ \__,_|_|  \__,_|___/___/_|\___| | .__/ \__,_|_|  |_|\_\ 
                                            | |                     
                                            |_| 
    """)
    game_scenario = '''Idea Credit: Jurassic Park by Steven Spielberg
          You are one of the lucky few who had the opportunity to visit the dinosaur island theme park, Jurassic Park!
          During your visit the park's power went down and some of the dinosaurs escaped.
          Run around the park until the rescue helicopter can pick you up.
          Survive using any means possible. Good Luck!'''
    print(game_scenario)
    return game_scenario


def print_map_appearance(saved_game):
    """Print the appearances of each map cell.

    A well formed map is a list of 4 lists of 4 dictionaries.
    The first list refers to the map rows. The nested list refers to the map columns.
    The dictionaries refer to the information of each cell. Each dictionary contains an appearance and a description.
    The appearance of a cell will be [ ] if empty and [X] if the character is inside it.
    PARAM: saved_game, a dictionary
    PRECONDITION: saved_game must have a username(string), hp(int), row_loc(int), col_loc(int), sud_map(well formed map)
    POSTCONDITION: print the appearance of the sud_map
    RETURN: string, a visual of the game map
    """
    print("Map:")
    map_visual = ""
    for rows in saved_game["sud_map"]:
        for col in rows:
            map_visual += col["appearance"]
        map_visual += "\n"
    print(map_visual)
    return map_visual


def print_description(saved_game):
    """Print the description of the map cell containing the character.

    A well formed map is a list of list of dictionaries.
    The first list refers to the map rows. The nested list refers to the map columns.
    The dictionaries refer to the information of each cell. Each dictionary contains an appearance and a description.
    The appearance of a cell will be [ ] if empty and [X] if the character is inside it.
    PARAM: saved_game, a dictionary
    PRECONDITION: saved_game must have a username(string), hp(int), row_loc(int), col_loc(int), sud_map(well formed map)
    POSTCONDITION: print the description of the map cell the character is in
    RETURN: string, the description of the map cell the character is in
    """
    print("Narrative: ")
    location_description = "   " + saved_game["sud_map"][saved_game['row_loc']][saved_game["col_loc"]]["description"]
    print(location_description)
    return location_description


def player_next_action(saved_game):
    """Get the user input for their next action.

    valid next actions are: 'q', 'n', 'e', 's', 'w'
    If the user input is 'n' move their character north.
    If the user input is 'e' move their character east.
    If the user input is 's' move their character south.
    If the user input is 'w' move their character west.
    If the user input is 'q' print a closing statement.
    If the user input is not a valid input, recursively call the function until they give a valid output.
    PARAM: saved_game, a dictionary
    PRECONDITION: saved_game must have a username(string), hp(int), row_loc(int), col_loc(int), sud_map(well formed map)
    POSTCONDITION: get the action for the users next action
    RETURN: the users next action which is of type string
    """
    print("Action: ")
    action = input("   Where do you want to go?"
                   "(q to quit game, n to go north, e to go east, s to go south, w to go west): ")
    action = action.lower()
    action = action.strip()
    if action == 'q':
        print("Thanks for playing. See you soon!")
        return action
    elif action == 'n' or action == 'e' or action == 's' or action == 'w':
        if move_character(action, saved_game):
            dinosaur_interaction(saved_game)
        return action
    else:
        print("THIS COMMAND DOESN'T WORK. PLEASE TRY AGAIN.")
        return player_next_action(saved_game)


def move_character(action, saved_game):
    """Change the row and column location of the character and update the map appearance.

    The character can only move 1 row or 1 column away at a time.
    If the character tries moving past any boarder of the map a error statement will be printed
    and the function will .
    Otherwise, the character will move, the map will be updated, and the function will return true.
    return false
    PARAM: action, a string of length one. saved_game, a dictionary
    PRECONDITION: saved_game must have a username(string), hp(int), row_loc(int), col_loc(int), sud_map(well formed map)
                  action must be 'n', 'e', 's', or 'w'
    POSTCONDITION: save the characters new location and change the appearance of the map
    RETURN: boolean, representing if the move was valid or not.
    """
    print("Result:")
    if action == "n":
        if saved_game["row_loc"] == 0:
            print("   You can't move farther North.")
            return False
        else:
            saved_game["sud_map"][saved_game["row_loc"]][saved_game["col_loc"]]["appearance"] = "[ ]"
            saved_game["row_loc"] -= 1
            saved_game["sud_map"][saved_game["row_loc"]][saved_game["col_loc"]]["appearance"] = "[X]"
            return True
    elif action == "e":
        if saved_game["col_loc"] == 3:
            print("   You can't move farther East.")
            return False
        else:
            saved_game["sud_map"][saved_game["row_loc"]][saved_game["col_loc"]]["appearance"] = "[ ]"
            saved_game["col_loc"] += 1
            saved_game["sud_map"][saved_game["row_loc"]][saved_game["col_loc"]]["appearance"] = "[X]"
            return True
    elif action == "s":
        if saved_game["row_loc"] == 3:
            print("   You can't move farther South.")
            return False
        else:
            saved_game["sud_map"][saved_game["row_loc"]][saved_game["col_loc"]]["appearance"] = "[ ]"
            saved_game["row_loc"] += 1
            saved_game["sud_map"][saved_game["row_loc"]][saved_game["col_loc"]]["appearance"] = "[X]"
            return True
    elif action == "w":
        if saved_game["col_loc"] == 0:
            print("   You can't move farther West.")
            return False
        else:
            saved_game["sud_map"][saved_game["row_loc"]][saved_game["col_loc"]]["appearance"] = "[ ]"
            saved_game["col_loc"] -= 1
            saved_game["sud_map"][saved_game["row_loc"]][saved_game["col_loc"]]["appearance"] = "[X]"
            return True


def dinosaur_interaction(saved_game):
    """Determine if the character will run into a dinosaur.

    There is a 10% chance a character will run into a dinosaur
    If the character doesnt run into a dinosaur increase its hp by 1 without exceeding its max hp of 10.
    If the character runs into a dinosaur the function will return True,
    If the character doesnt run into a dinosaur the function will return False
    PARAM: saved_game, a dictionary
    PRECONDITION: saved_game must have a username(string), hp(int), row_loc(int), col_loc(int), sud_map(well formed map)
    POSTCONDITION: have the character either run into a dinosaur or not
    RETURN: boolean, representing if a character encountered a dinosaur or not
    """
    chance = random.random()
    if chance <= 0.1:
        list_of_dinos = ['T-Rex', 'Velociraptor', 'Triceratop']
        random_dino = random.randint(0, 2)
        print("   You ran into a " + list_of_dinos[random_dino])
        fight_or_run(saved_game)
        return True
    else:
        if saved_game["hp"] < 10:
            saved_game["hp"] += 1
            print("   You moved safely and gained 1 hp.")
        else:
            print("   You moved safely and are at max hp.")
        return False


def fight_or_run(saved_game):
    """Ask the user if he wants to run of fight from the dinosaur.

    If the user runs the function will return True
    If the user fights the function will return False
    If the user doesn't input one of: 'f', 'F', 'r', or 'R', the function will keep asking for inputs until one is given
    PARAM: saved_game, a dictionary
    PRECONDITION: saved_game must have a username(string), hp(int), row_loc(int), col_loc(int), sud_map(well formed map)
    POSTCONDITION: have the character either run or fight
    RETURN: boolean, representing if the user fights or runs
    """
    action = input("   Press f to fight or r to run: ")
    action = action.lower()
    action = action.strip()
    while not (action == 'f' or action == 'r'):
        action = input("   Invalid Input. Press f to fight or r to run: ")
        action = action.lower()
        action = action.strip()
    if action == 'r':
        run(saved_game)
        return True
    else:
        fight(saved_game)
        return False


def run(saved_game):
    """Determine if the character successfully runs from the dinosaur.

    The character will have a 10% chance of being caught when trying to run.
    If caught the dinosaur will deal 1-4 damage to the character.
    If the character dies from the caught damage, end the game.
    PARAM: saved_game, a dictionary
    PRECONDITION: saved_game must have a username(string), hp(int), row_loc(int), col_loc(int), sud_map(well formed map)
    POSTCONDITION: have the character take damage if caught when trying to run
    RETURN: none
    """
    chance = random.random()
    if chance < 0.1:
        print("   You got caught")
        dmg = random.randint(1, 4)
        saved_game["hp"] -= dmg
        print("   The dinosaur did", dmg, "damage to you")
        if saved_game["hp"] < 1:
            print("   You were eaten")
            print("GAME OVER")
    else:
        list_of_escapes = ['   The guy beside you trips.', '   *BANG* The dinosaur got shot by the rescue helicopter.',
                           '   You found a car.']
        random_escape = random.randint(0, 2)
        print(list_of_escapes[random_escape] + " You got away safely!")


def fight(saved_game):
    """Conduct a fight with the character and the dinosaur until one is dead.

    The user will deal 1-6 damage to the dinosaur then the dinosaur will deal 1-6 damage to the user.
    The step above repeats until one is dead.
    If the dinosaur dies, return True
    If the character dies, return False
    PARAM: saved_game, a dictionary
    PRECONDITION: saved_game must have a username(string), hp(int), row_loc(int), col_loc(int), sud_map(well formed map)
    POSTCONDITION: conduct a fight to the death between a dinosaur and the user
    RETURN: boolean, representing if the dinosaur died
    """
    dinosaur_hp = 5
    print("   FIGHT TO THE DEATH! Dinosaur hp: 5, Your hp:", saved_game["hp"])
    while dinosaur_hp > 0 and saved_game["hp"] > 0:
        # Character attacks
        character_dmg = random.randint(1, 6)
        dinosaur_hp -= character_dmg
        print("   You dealt", character_dmg, "to the dinosaur.", end=" ")
        if dinosaur_hp > 0:
            print("   The dinosaur has", dinosaur_hp, "hp remaining")
        else:
            print("   You have slain the dinosaur.")
            return True
        # Dinosaur attacks
        dinosaur_dmg = random.randint(1, 6)
        saved_game["hp"] -= dinosaur_dmg
        print("   The dinosaur dealt", dinosaur_dmg, "to you.", end=" ")
        if saved_game["hp"] > 0:
            print("   You have", saved_game["hp"], "hp remaining")
        else:
            print("   You have been slain.")
            print("GAME OVER")
            return False


def save(saved_game):
    """Save the saved_game (dictionary) onto the users json file

    PARAM: saved_game, a dictionary
    PRECONDITION: saved_game must have a username(string), hp(int), row_loc(int), col_loc(int), sud_map(well formed map)
    POSTCONDITION: save the users game onto their json file
    RETURN: none
    """
    filename = saved_game["username"] + ".json"
    with open(filename, "w") as file_object:
        json.dump(saved_game, file_object)


def reload_game(saved_game):
    """Save a new game to the users json file

    PARAM: saved_game, a dictionary
    PRECONDITION: saved_game must have a username(string), hp(int), row_loc(int), col_loc(int), sud_map(well formed map)
    POSTCONDITION: save a new game onto the users json file
    RETURN: none
    """
    saved_game["hp"] = 10
    saved_game["sud_map"][saved_game["row_loc"]][saved_game["col_loc"]]["appearance"] = "[ ]"
    saved_game["row_loc"] = 0
    saved_game["col_loc"] = 0
    saved_game["sud_map"][saved_game["row_loc"]][saved_game["col_loc"]]["appearance"] = "[X]"
    save(saved_game)


def conduct_one_turn(saved_game):
    """Conduct one turn of the game

    One turn consists of:
    printing the map, printing your current hp, printing the map cell description, asking for the next players action,
    save the game, and return the players action.
    If the character dies during players next action, the function will reset the game to its starting values.
    PARAM: saved_game, a dictionary
    PRECONDITION: saved_game must have a username(string), hp(int), row_loc(int), col_loc(int), sud_map(well formed map)
    POSTCONDITION: conduct one turn of the game
    RETURN: the users last action of type string
    """
    print("---------- Turn Start ----------")
    print_map_appearance(saved_game)
    print("Character Info: \n   You have", saved_game["hp"], "hp")
    print_description(saved_game)
    checker = player_next_action(saved_game)
    save(saved_game)
    if saved_game["hp"] < 1:
        reload_game(saved_game)
        return 'q'
    print("---------- Turn End ----------")
    return checker


def main():
    """Execute the code."""
    user_game = start_game()
    checker = "a"
    while not checker == 'q':
        checker = conduct_one_turn(user_game)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    main()
