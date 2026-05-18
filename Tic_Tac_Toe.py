# Tic Tac Toe - Console Game (Beginner Friendly)

# Board positions:
# 1 | 2 | 3
# ---------
# 4 | 5 | 6
# ---------
# 7 | 8 | 9

board = [' ' for _ in range(9)]


def show_board():
    print()
    print(board[0], '|', board[1], '|', board[2])
    print('--+---+--')
    print(board[3], '|', board[4], '|', board[5])
    print('--+---+--')
    print(board[6], '|', board[7], '|', board[8])
    print()


def is_winner(player):
    win_combos = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
        (0, 4, 8), (2, 4, 6)              # diagonals
    ]
    for a, b, c in win_combos:
        if board[a] == board[b] == board[c] == player:
            return True
    return False


def is_draw():
    return ' ' not in board


current_player = 'X'

print("Welcome to Tic Tac Toe!")
print("Enter positions from 1 to 9 as shown below:")
print("1 | 2 | 3")
print("4 | 5 | 6")
print("7 | 8 | 9")

while True:
    show_board()

    try:
        pos = int(input(f"Player {current_player}, enter position (1-9): ")) - 1
        if pos < 0 or pos > 8:
            print("Invalid position. Choose 1-9.")
            continue
        if board[pos] != ' ':
            print("Position already taken. Try again.")
            continue
    except ValueError:
        print("Please enter a number between 1 and 9.")
        continue

    board[pos] = current_player     

    if is_winner(current_player):
        show_board()
        print(f"Player {current_player} wins! 🎉")
        break

    if is_draw():
        show_board()
        print("It's a draw!")
        break

    current_player = 'O' if current_player == 'X' else 'X'