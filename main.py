import numpy as np

# Functions


def ship_placement(player):
    for i in range(11):
        for b in range(11):
            if i != 0 and b != 0:
                player["cords"].update([((i, b), "-")])
            elif i == 0:
                player["cords"].update([((i, b), b)])
            if b == 0:
                player["cords"].update([((i, b), i)])
    print_board(player)


def print_board(player):
    moves = 0
    counter = 0
    while moves != 20:
        x = int(input(": "))
        y = int(input(": "))
        if x in possible_moves and y in possible_moves:
            player["cords"].update([((y, x), "X")])
            for i in range(11):
                for b in range(11):
                    print(player["cords"][(i, b)], end=" ")
                    counter += 1
                    if counter % 11 == 0:
                        print("\n")
            moves += 1
        else:
            print("Try again")
    for i in range(100):
        print()


def allowed_moves():
    moves = []
    for i in range(1, 11):
        for b in range(1, 11):
            moves.append([i, b])
    available_moves = np.array(moves)
    return available_moves


def player_guess(enemy, player):
    while True:
        x = int(input(": "))
        y = int(input(": "))
        if x in possible_moves and y in possible_moves:
            if enemy["cords"][(y, x)] == "X":
                player["Hits"].append((y, x))
                print("You hit an enemy ship! Congratulations")
                print(player)
                break
            else:
                player["Misses"].append((y, x))
                print("You missed the ship :(")
                print("Don't worry you'll get it next time!")
                print(player)
                break
        else:
            print("try again")


# Player dictionaries
player_1 = {"cords": {}}
player_2 = {"cords": {}}
board_checker_1 = {"cords": {}}
board_checker_2 = {"cords": {}}
player_1_shots = {"Misses": [], "Hits": []}
player_2_shots = {"Misses": [], "Hits": []}
possible_moves = allowed_moves()

# Main action
print("Start by placing your ships on the game board. You will need to cover 20 tiles in total. "
      "Here are the ship requirements:\n")
print("--> x4 one tile-ships")
print("--> x3 2 tile-ships")
print("--> x2 three tile-ships")
print("--> x1 4 tile-ships\n")
print("-----------------------------------------------------------------------------------------------------------")
print("Player 1 turn")
ship_placement(player_1)
print("Player 2 turn")
ship_placement(player_2)

while True:
    # Создать универсальную функцию
    print("Player 1 turn")
    player_guess(player_2, player_1_shots)
    print("-----------------------------------------------------------------------------------------------------------")
    if len(player_1_shots["Hits"]) == 20:
        print("Player 1 won")
        break
    print("Player 2 turn")
    player_guess(player_1, player_2_shots)
    print("-----------------------------------------------------------------------------------------------------------")
    if len(player_2_shots["Hits"]) == 20:
        print("Player 2 won")
        break
