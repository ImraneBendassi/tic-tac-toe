import tkinter
from tkinter import messagebox

PLAYER_X = 'X'
PLAYER_O = 'O'

class TicTacToe:
    def __init__(self):
        self.buttons = []
        self.current_player = PLAYER_X
        self.win = False
        self.draw_grid()

    def print_winner(self):
        self.win = True
        messagebox.showinfo("Fin de partie", f"Le joueur {self.current_player} a gagné le jeu!")

    def switch_player(self):
        self.current_player = PLAYER_O if self.current_player == PLAYER_X else PLAYER_X

    def check_win(self):
        for i in range(3):
            
            if self.buttons[i][0]['text'] == self.buttons[i][1]['text'] == self.buttons[i][2]['text'] == self.current_player \
                    or self.buttons[0][i]['text'] == self.buttons[1][i]['text'] == self.buttons[2][i]['text'] == self.current_player:
                self.print_winner()
                return
        
        
        if self.buttons[0][0]['text'] == self.buttons[1][1]['text'] == self.buttons[2][2]['text'] == self.current_player \
                or self.buttons[0][2]['text'] == self.buttons[1][1]['text'] == self.buttons[2][0]['text'] == self.current_player:
            self.print_winner()
            return

        
        count = sum(1 for row in self.buttons for button in row if button['text'] in (PLAYER_X, PLAYER_O))
        if count == 9:
            messagebox.showinfo("Fin de partie", "Match nul!")

    def place_symbol(self, row, column):
        clicked_button = self.buttons[column][row]
        if clicked_button['text'] == "" and not self.win:
            clicked_button.config(text=self.current_player)
            self.check_win()
            self.switch_player()

    def draw_grid(self):
        for column in range(3):
            buttons_in_cols = []
            for row in range(3):
                button = tkinter.Button(
                    root, font=("Arial", 50),
                    width=5, height=3,
                    command=lambda r=row, c=column: self.place_symbol(r, c)
                )
                button.grid(row=row, column=column)
                buttons_in_cols.append(button)
            self.buttons.append(buttons_in_cols)


root = tkinter.Tk()
root.title("TicTacToe")
root.minsize(500, 500)


tic_tac_toe_game = TicTacToe()


root.mainloop()


