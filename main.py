import numpy as np

game_board = np.array([
        ["", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"],
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

# Ship placements & printing/clearing the board


def allowed_moves():
    possible_moves = []
    for i in range(1, 11):
        for b in range(1, 11):
            possible_moves.append([i, b])
    available_moves = np.array(possible_moves)
    return available_moves


def player_ship_placement(player):
    while len(player) != 3:
        print("Enter coords")
        x = int(input(": "))
        y = int(input(": "))
        if x in allowed_moves() and y in allowed_moves() and player.count([y, x]) == 0:
            player.append([y, x])
            game_board[x][y] = "X"
            board()
        else:
            print("Try again those coordinates don't work")
    for i in range(100):
        print()
    clearing_board()


def clearing_board():
    while np.count_nonzero(game_board == "X") != 0 or np.count_nonzero(game_board == "H") != 0:
        for row_index, row in enumerate(game_board):
            for col_index, cell in enumerate(row):
                if cell == "X" or cell == "H":
                    game_board[row_index][col_index] = "-"
    return game_board


def board():
    for i in range(len(game_board)):
        print(*game_board[i])


def checking_for_hit(player):
    for i in range(len(player)):
        if len(player[i]) == 2:
            game_board[player[i][1]][player[i][0]] = "X"
            board()
        elif len(player[i]) == 3:
            game_board[player[i][1]][player[i][0]] = "H"
            board()


def player_turn(player, enemy):
    print("|Ship checker|\n")
    clearing_board()
    checking_for_hit(player)
    while True:
        x = int(input(": "))
        y = int(input(": "))
        if x in allowed_moves() and y in allowed_moves() and player.count([y, x]) == 0:
            if [y, x] in enemy:
                enemy.remove([y, x])
                player.append([y, x, "H"])
                print("You hit an enemy ship")
                clearing_board()
                checking_for_hit(player)
                break
            else:
                player.append([y, x])
                clearing_board()
                checking_for_hit(player)
                break
        else:
            print("try again")






player_one_cords = []
player_two_cords = []

player_one_moves = []
player_two_moves = []

print("|Player 1 turn|:\n")
player_ship_placement(player_one_cords)
print("|Player 2 turn|:\n")
player_ship_placement(player_two_cords)

flag = True
while flag:
    print("Player 1 turn")
    player_turn(player_one_moves, player_two_cords)
    print("---------------------------------------------------------------------------------"
          "-----------------------------------------------")
    print("Player 2 turn")
    player_turn(player_two_moves, player_one_cords)
    print("---------------------------------------------------------------------------------"
          "-----------------------------------------------")
