import random

def print_board(board):
    print("            Kolom")
    print("            1   2   3 ")
    print("          -------------")
    for idx, row in enumerate(board):
        print(f"Baris {idx + 1}   | " + " | ".join(row) + " |")
        if idx < 2:
            print("          -------------")

def check_winner(board):
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] != ' ':
            return row[0]
    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != ' ':
            return board[0][col]
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]
    return None

def is_board_full(board):
    for row in board:
        for cell in row:
            if cell == ' ':
                return False
    return True

def player_move(board, current_player):
    while True:
        try:
            row = int(input("Masukkan nomor baris (1, 2, atau 3): ")) - 1
            col = int(input("Masukkan nomor kolom (1, 2, atau 3): ")) - 1
            if row not in range(3) or col not in range(3):
                print("Masukkan hanya angka 1, 2, atau 3.")
                continue
            if board[row][col] == ' ':
                board[row][col] = current_player
                break
            else:
                print("Tempat sudah diisi. Pilih tempat lain.")
        except ValueError:
            print("Masukkan hanya angka 1, 2, atau 3.")

def computer_move(board):
    empty_cells = [(r, c) for r in range(3) for c in range(3) if board[r][c] == ' ']
    row, col = random.choice(empty_cells)
    board[row][col] = 'O'
    print(f"Komputer memilih baris {row + 1} dan kolom {col + 1}.")

def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'  # Pemain selalu mulai pertama

    while True:
        print_board(board)

        if current_player == 'X':
            player_move(board, current_player)
        else:
            computer_move(board)

        winner = check_winner(board)
        if winner:
            print_board(board)
            if winner == 'X':
                print("Selamat! Pemenangnya adalah Pemain!")
            else:
                print("Komputer menang!")
            break
        elif is_board_full(board):
            print_board(board)
            print("Permainan berakhir. Ini hasil seri!")
            break

        current_player = 'O' if current_player == 'X' else 'X'

play_game()
