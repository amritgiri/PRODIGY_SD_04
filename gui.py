import tkinter as tk
from tkinter import ttk

def is_valid(board, row, col, num):
    return(
        all(num != board[row][i] for i in range(9)) and
        all(num != board[i][col] for i in range(9)) and
        all(num != board[row // 3 *3 + i // 3][col // 3 *3 + i % 3] for i in range(9))
    )

def solve(board):
    empty = find_empty(board)
    if not empty:
        return True
    
    row, col = empty

    for num in range(1,10):
        if is_valid(board, row, col, num):
            board[row][col] = num

            if solve(board):
                return True
            
            board[row][col] = 0
    return False


def find_empty(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i,j)
    return None

def display_board(board):
    for row in board:
        print("".join(map(str,row)))

def solve_and_display():
    # get entry values
    for i in range(9):
        for j in range(9):
            entry_value = entry_grid[i][j].get()
            if entry_value.isdigit():
                example_board[i][j] = int(entry_value)
            else:
                example_board[i][j] = 0
    
    # solve the puzzle
    solve(example_board)

    # display solved
    for i in range(9):
        for j in range(9):
            entry_grid[i][j].delete(0,tk.END)
            entry_grid[i][j].insert(0, example_board[i][j])

def clear_entries():
    # Clear all entry widgets
    for i in range(9):
        for j in range(9):
            entry_grid[i][j].delete(0, tk.END)


# initilization of example_board
example_board = [[0] *9 for _ in range(9)]

# GUI
window = tk.Tk()
window.title('Sudoku Solver')

entry_grid = [[tk.Entry(window, width= 2, font= ('Ubuntu', 16)) for _ in range(9)] for _ in range(9)]

# place entry widget in the grid

for i in range(9):
    for j in range(9):
        entry_grid[i][j].grid(row= i, column= j, padx=2, pady=2)

# Create Solve button
solve_button = tk.Button(window, text="Solve", command=solve_and_display)
solve_button.grid(row=9, column=2, columnspan=2)

# Create Clear button
clear_button = tk.Button(window, text="Clear", command=clear_entries)
clear_button.grid(row=9, column=5, columnspan=2)


window.mainloop()