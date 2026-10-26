def print_board(board):
    print()
    for row in board:
        print(" | ".join(row))
        print("--+--+--")
    print()

def check_winner(board,player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range (3)):
            return True

        if all(board[i][i] == player for i in range (3)):
            return True

        if all(board[i][2-1] == player for i in range (3)):
            return True


    return False 


def main():
    board = [[" " for _ in range (3)] for _ in range(3)]
    player = "X"
    moves = 0

    while True: 
        print_board(board)
        print(f"Player {player}, it's your turn!")

        try:
            row = int(input("Enter row (1-3):")) - 1
            col = int(input("Enter column (1-3):")) - 1
        except ValueError:
            print("Please enter numbers only.")
            continue
        if not (0 <= row < 3 and 0 <= col < 3):
            print("Invalid position. Choose 1, 2 or 3.")
            continue
        if board[row][col] !=" ":
            print("That position is already taken!")
            continue
        board[row][col] = player
        moves += 1

        if check_winner(board,player):
            print_board(board)
            print(f"Congratulations! Player {player} wins!")
            break
        if moves == 9:
            print_board(board)
            print("It's a draw!")
            break
        player = "O" if player == "X" else "X"
if __name__ == "__main__":
    main()      

