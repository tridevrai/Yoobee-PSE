# Activity Week 10-3: Develop a Tic-tac-toe Game Using Python 
# Develop a code decomposition and enhance your coding style. Once completed, share the GitHub link. (Estimated development time: 20 minutes)
# See link: https://en.wikipedia.org/wiki/Tic-tac-toe


tic_tac_toe_board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

def print_board(board):
    for row in board:
        print("|".join(row)) # join the row with |
        print("-" * 5) # print a line of 5 dashes

def check_winner(board, player):
    return (
        check_all_cells_in_row_are_the_same(board, player) or 
        check_all_cells_in_column_are_the_same(board, player) or 
        check_all_cells_in_diagonal_are_the_same(board, player)
    )


def check_all_cells_in_row_are_the_same(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    return False

def check_all_cells_in_column_are_the_same(board, player):
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    return False

def check_all_cells_in_diagonal_are_the_same(board, player):
    if all(board[i][i] == player for i in range(3)): # check diagonal (0,0), (1,1), (2,2)
        return True
    if all(board[i][2 - i] == player for i in range(3)): # check diagonal (0,2), (1,1), (2,0)
        return True
    return False

def is_board_full(board):
    for row in board:
        for cell in row:
            if cell == " ":
                return False
    return True

def main():
    current_player = "X"
    while True:
        print_board(tic_tac_toe_board)
        print(f"Player {current_player}'s turn")
        row,col = map(int, input("Enter the row, col like 0,0:   ").split(","))
        if tic_tac_toe_board[row][col] == " ":
            tic_tac_toe_board[row][col] = current_player
            if check_winner(tic_tac_toe_board, current_player):
                print_board(tic_tac_toe_board)
                print(f"Player {current_player} wins!")
                break
            if is_board_full(tic_tac_toe_board):
                print_board(tic_tac_toe_board)
                print("It's a tie!")    
                break
            current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    main()  