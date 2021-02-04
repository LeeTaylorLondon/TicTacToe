from typing import NoReturn, Tuple

board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

def print_board() -> NoReturn:
    # Print indexes for player to select
    print("Number inputted selects tile shown below:")
    indexes = [str(x) for x in range(1, 10)]
    for i in range(0, 9, 3):
        print(f"{'|'.join(indexes[i:i+3])}")
    print()
    # Print current state of the board
    print("Current board state:")
    for i in range(0, 9, 3):
        print(f"{'|'.join(board[i:i+3])}")


def check_end() -> Tuple[bool, str]:
    # 5 or more empty spaces indicates no player's have won yet
    if (board.count(" ") >= 5):
        return False, ""
    # Win check horizontal
    for i in range(0, 9, 3):
        for char in "OX":
            if (board[i:i+3].count(char) == 3):
                return True, char
    # Win check vertical
    for i in range(3):
        for char in "OX":
            if (board[0 + i] == char) and (board[3 + i] == char) and (board[6 + i] == char):
                return True, char
    # Win check diagonal
    for char in "OX":
        if (board[0] == char) and (board[4] == char) and (board[8] == char):
            return True, char
        if (board[6] == char) and (board[4] == char) and (board[2] == char):
            return True, char
    # Draw check
    if (board.count(" ") == 0):
        return True, "No-one"
    return False, ""

def take_turn(player):
    choice = 0
    # Validate choice both for range and if already taken
    while not (0 < choice < 10):
        choice = int(input("Select tile 1-9: "))
        if (board[choice - 1] != " "):
            print("Tile is already taken, choose another!")
            choice = 0
    # Mark board coordinate accordingly
    if (player == 1):
        board[choice - 1] = "X"
    else:
        board[choice - 1] = "O"
    # Check for draw/win
    check_end()


# Main game logic

end = False  # indicates whether game has ended or not
player = 1  # indicates which player's turn
turn = 1  # turn number
while (check_end()[0] == False):
    # P1 turn, P2 turn, ...
    print(f"Turn Number: {turn}")
    print_board()
    take_turn(player)
    player = not player
    turn += 1
print_board()
print("Winner: ", check_end()[1])



