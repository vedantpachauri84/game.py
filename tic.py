import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import random
import winsound  # Only works on Windows

import numpy as np




class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("game of kings - 😎 vs 🤖")
        self.board = [""] * 9
        self.buttons = []
        self.player = "😎"
        self.ai = "🤖"
        self.player_score = 0
        self.ai_score = 0
        self.mode = None
        self.create_mode_selector()

    def create_mode_selector(self):
        self.mode_frame = tk.Frame(self.root)
        self.mode_frame.grid(row=0, column=0, columnspan=30)
        tk.Label(self.mode_frame, text="Choose Mode:", font=("Arial", 140)).pack()
        tk.Button(self.mode_frame, text="vedantpachauri vs AI",width=16,height=3, command=self.start_ai_mode).pack(pady=50)
        tk.Button(self.mode_frame, text="Player vs Player",width=16,height=3, command=self.start_pvp_mode).pack(pady=50)

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

        quit_button = tk.Button( text="Quit", font=("Arial", 12), command=self.root.destroy)
        quit_button.grid(row=4, column=0, columnspan=3, pady=10)

    def get_score_text(self):
        return f"😎: {self.player_score}   🤖: {self.ai_score}" if self.mode == "AI" else f"Player X: {self.player_score}   Player O: {self.ai_score}"

    def update_scoreboard(self):
        self.score_label.config(text=self.get_score_text())

    def create_board(self):
        for i in range(9):
            btn = tk.Button(self.root, text="", font=("Arial", 24), width=18, height=6,
                            command=lambda i=i: self.make_move(i))
            btn.grid(row=i//3, column=i%3)
            self.buttons.append(btn)


    def make_move(self, index):
        if self.board[index] == "":
            self.play_sound("click")
            self.board[index] = self.player
            self.buttons[index].config(text=self.player)
            if self.check_winner(self.player):
                self.player_score += 1
                self.update_scoreboard()
                self.play_sound("win")
                self.end_game(f"{self.player} wins!")
            elif "" not in self.board:
                self.play_sound("draw")
                self.end_game("It's a draw!")
            else:
                if self.mode == "AI":
                    self.ai_move()
                else:
                    self.player = "🤖" if self.player == "😎" else "😎"

    def ai_move(self):
        empty = [i for i, val in enumerate(self.board) if val == ""]
        index = random.choice(empty)
        self.play_sound("click")
        self.board[index] = self.ai
        self.buttons[index].config(text=self.ai)
        if self.check_winner(self.ai):
            self.ai_score += 1
            self.update_scoreboard()
            self.play_sound("lose")
            self.end_game(f"{self.ai} wins!")
        elif "" not in self.board:
            self.play_sound("draw")
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
        self.player = "😎"

    def play_sound(self, event):
        try:
            if event == "click":
                winsound.PlaySound("SystemAsterisk", winsound.SND_ALIAS | winsound.SND_ASYNC)
            elif event == "win":
                winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS | winsound.SND_ASYNC)
            elif event == "lose":
                winsound.PlaySound("SystemHand", winsound.SND_ALIAS | winsound.SND_ASYNC)
            elif event == "draw":
                winsound.PlaySound("SystemQuestion", winsound.SND_ALIAS | winsound.SND_ASYNC)
        except:
            pass  # Sound may not work on non-Windows systems

# Run the game
root = tk.Tk()
game = TicTacToe(root)
root.mainloop()
