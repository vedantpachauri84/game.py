import tkinter as tk
from tkinter import messagebox
import random

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.board = [""] * 9
        self.buttons = []
        self.player = "X"
        self.ai = "O"
        self.player_score = 0
        self.ai_score = 0
        self.mode = None
        self.create_mode_selector()

    def create_mode_selector(self):
        self.mode_frame = tk.Frame(self.root)
        self.mode_frame.grid(row=0, column=0, columnspan=3)
        tk.Label(self.mode_frame, text="Choose Mode:", font=("Arial", 14)).pack()
        tk.Button(self.mode_frame, text="Player vs AI", command=self.start_ai_mode).pack(pady=5)
        tk.Button(self.mode_frame, text="Player vs Player", command=self.start_pvp_mode).pack(pady=5)

    def start_ai_mode(self):
        self.mode = "AI"
        self.mode_frame.destroy()
        self.create_scoreboard()
        self.create_board()

    def start_pvp_mode(self):
        self.mode = "PVP"
        self.mode_frame.destroy()
        self.create_scoreboard()
        self.create_board()

    def create_scoreboard(self):
        self.score_label = tk.Label(self.root, text=self.get_score_text(), font=("Arial", 14))
        self.score_label.grid(row=3, column=0, columnspan=3)

    def get_score_text(self):
        return f"Player X: {self.player_score}   Player O: {self.ai_score}" if self.mode == "PVP" else f"Player: {self.player_score}   AI: {self.ai_score}"

    def update_scoreboard(self):
        self.score_label.config(text=self.get_score_text())

    def create_board(self):
        for i in range(9):
            btn = tk.Button(self.root, text="", font=("Arial", 24), width=24, height=8,
                            command=lambda i=i: self.make_move(i))
            btn.grid(row=i//3, column=i%3)
            self.buttons.append(btn)

    def make_move(self, index):
        if self.board[index] == "":
            self.board[index] = self.player
            self.buttons[index].config(text=self.player)
            if self.check_winner(self.player):
                self.player_score += 1
                self.update_scoreboard()
                self.end_game(f"{self.player} wins!")
            elif "" not in self.board:
                self.end_game("It's a draw!")
            else:
                if self.mode == "AI":
                    self.ai_move()
                else:
                    self.player = "O" if self.player == "X" else "X"

    def ai_move(self):
        empty = [i for i, val in enumerate(self.board) if val == ""]
        index = random.choice(empty)
        self.board[index] = self.ai
        self.buttons[index].config(text=self.ai)
        if self.check_winner(self.ai):
            self.ai_score += 1
            self.update_scoreboard()
            self.end_game("AI wins!")
        elif "" not in self.board:
            self.end_game("It's a draw!")

    def check_winner(self, player):
        wins = [(0,1,2), (3,4,5), (6,7,8),
                (0,3,6), (1,4,7), (2,5,8),
                (0,4,8), (2,4,6)]
        return any(all(self.board[i] == player for i in combo) for combo in wins)

    def end_game(self, result):
        play_again = messagebox.askyesno("Game Over", f"{result}\nDo you want to play again?")
        if play_again:
            self.reset_board()
        else:
            self.root.destroy()

    def reset_board(self):
        self.board = [""] * 9
        for btn in self.buttons:
            btn.config(text="")
        self.player = "vedant"

# Run the game
root = tk.Tk()
game = TicTacToe(root)
root.mainloop()