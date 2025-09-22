
def display_board(board):
    """Displays the current Tic Tac Toe board"""
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")

def player_input(player, board):
    """Gets a valid move from the current player"""
    while True:
        try:
            pos = int(input(f"Player {player} turn. Choose a position (1-9): ")) - 1
            if pos < 0 or pos > 8:
                print("Invalid position! Choose 1-9.")
            elif board[pos] != " ":
                print("Position already taken! Choose another.")
            else:
                return pos
        except ValueError:
            print("Please enter a number from 1 to 9.")

def check_win(board):
    """Check if there is a winner or tie"""
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  
        [0, 4, 8], [2, 4, 6]              
    ]
    for condition in win_conditions:
        a, b, c = condition
        if board[a] == board[b] == board[c] and board[a] != " ":
            return board[a]  
    if " " not in board:
        return "Tie"
    return None  

def play():
    """Main function to play the game"""
    board = [" "] * 9
    current_player = "X"
    winner = None

    display_board(board)
    
    while winner is None:
        move = player_input(current_player, board)
        board[move] = current_player
        display_board(board)
        winner = check_win(board)

        if winner is None:
            current_player = "O" if current_player == "X" else "X"

    if winner == "Tie":
        print("The game is a tie!")
    else:
        print(f"Congratulations! Player {winner} wins!")

if __name__ == "__main__":
    play()
