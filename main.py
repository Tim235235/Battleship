import numpy as np


def cords_list(possible_moves):
    for i in range(11):
        for b in range(11):
            possible_moves.append([i, b])
            available_moves = np.array(possible_moves)
            return available_moves


def player_ship_placement(player):
    while len(player) != 20:
        cords = int(input(": "))
        if available_moves:
            player[y][letter_to_number[x]] = "X"
            for d in range(len(player)):
                print(*player[d])
        else:
            print("try again")


def players_turn(player_checker, enemy):
    print("Checking Board")
    while True:
        x = input(": ")
        y = int(input(": "))
        if letter_to_number[x] < 11 and y < 11 and y > 0 and letter_to_number[x] > 0:
            if enemy[y][letter_to_number[x]] == "X":
                print("You hit an enemy ship")
                enemy[y][letter_to_number[x]] = "X"
                player_checker[y][letter_to_number[x]] = "H"
            elif enemy[y][letter_to_number[x]] == "-":
                enemy[y][letter_to_number[x]] = "X"
                player_checker[y][letter_to_number[x]] = "X"
            for d in range(len(player_checker)):
                print(*player_checker[d])
        else:
            print("Those coordinates don't exist. Try again")


def printing_board(player):
    for i in range(len(player)):
        print(*player[i])
# Main code


def main() -> None:
    print("\n|Each player will get 6 ships. Use the cords on the map to place your ship|\n")
    for i in range(len(player_1)):
        print(*player_1[i])

    # Getting ship placements
    print("Player 1 turn")
    player_ship_placement(player_1)
    for i in range(100):
        print()
    print("Player 2 turn")
    player_ship_placement(player_2)

    # Playing(main while loop)
    print("Time to play. Look at your checking board to find positions to attack. First one to destroy all ships wins!")

    printing_board(player_1_checker)

    flag = True
    while flag:
        print("Player 1 turn")
        printing_board(player_1_checker)
        players_turn(player_1_checker, player_2)
        if np.count_nonzero(player_1_checker == "H") == 20:
            print("player 1 won")
            break
        print("---------------------------------------------------------------------------------"
              "-----------------------------------------------")
        print("Player 2 turn")
        printing_board(player_2_checker)
        players_turn(player_2_checker, player_1)
        if np.count_nonzero(player_2_checker == "H") == 20:
            print("player 2 won")
            break



if __name__ == "__main__":
    player_one = []
    player_two = []

    player_1 = np.array([
        ["", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J"],
        ["1", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
        ["2", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
        ["3", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
        ["4", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
        ["5", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
        ["6", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
        ["7", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
        ["8", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
        ["9", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
        ["10", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"]
        ]
    )

    player_1_checker = np.array([
        ["", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J"],
        ["1", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
        ["2", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
        ["3", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
        ["4", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
        ["5", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
        ["6", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
        ["7", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
        ["8", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
        ["9", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
        ["10", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"]
    ]
    )

    player_2 = np.array([
        ["", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J"],
        ["1", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
        ["2", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
        ["3", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
        ["4", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
        ["5", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
        ["6", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
        ["7", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
        ["8", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
        ["9", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
        ["10", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"]
    ]
    )

    player_2_checker = np.array([
        ["", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J"],
        ["1", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
        ["2", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
        ["3", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
        ["4", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
        ["5", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
        ["6", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
        ["7", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
        ["8", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
        ["9", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
        ["10", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"]
    ]
    )
    letter_to_number = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "I": 9, "J": 10}

    main()
