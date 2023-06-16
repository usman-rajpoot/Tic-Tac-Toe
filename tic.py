import tkinter as tk
from tkinter import messagebox

class TicTacToeGUI:
    def __init__(self):
        self.board = [['' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
        self.root = tk.Tk()
        self.root.title("Tic Tac Toe")
        self.buttons = [[self.create_button(i, j) for j in range(3)] for i in range(3)]

    def create_button(self, row, col):
        button = tk.Button(self.root, text='', width=10, height=5,
                           command=lambda: self.handle_click(button, row, col))
        button.grid(row=row, column=col)
        return button

    def handle_click(self, button, row, col):
        if self.board[row][col] == '':
            self.board[row][col] = self.current_player
            button.config(text=self.current_player, state=tk.DISABLED)
            if self.check_winner(row, col):
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                self.reset_game()
            elif self.is_board_full():
                messagebox.showinfo("Game Over", "It's a tie!")
                self.reset_game()
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'

    def check_winner(self, row, col):
        symbol = self.current_player
        if (self.board[row][0] == self.board[row][1] == self.board[row][2] == symbol or
            self.board[0][col] == self.board[1][col] == self.board[2][col] == symbol or
            self.board[0][0] == self.board[1][1] == self.board[2][2] == symbol or
            self.board[0][2] == self.board[1][1] == self.board[2][0] == symbol):
            return True
        return False

    def is_board_full(self):
        for row in self.board:
            if '' in row:
                return False
        return True

    def reset_game(self):
        self.board = [['' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text='', state=tk.NORMAL)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    game = TicTacToeGUI()
    game.run()
