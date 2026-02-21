import tkinter as tk
from tkinter import messagebox
import copy

class Connect_4:
    def __init__(self):
        self.rows = 6
        self.cols = 7
        self.initial_grid = [[" " for _ in range(self.cols)] for _ in range(self.rows)]

    def current_player(self, state):
        count_X = sum(row.count('X') for row in state)
        count_O = sum(row.count('O') for row in state)
        return 'X' if count_X == count_O else 'O'

    def take_action(self, state, action):
        player, col = action
        new_state = [row[:] for row in state]
        for row in range(self.rows - 1, -1, -1):
            if new_state[row][col] == " ":
                new_state[row][col] = player
                break
        return new_state

    def available_actions(self, state):
        player = self.current_player(state)
        actions = []  
        for col in range(self.cols):  
            if state[0][col] == " ": 
                actions.append((player, col))  
        return actions 
    def check_terminal(self, state):
        for r in range(self.rows):
            for c in range(self.cols):
                if state[r][c] == " ": continue
                p = state[r][c]
                # Check 4 directions
                if c + 3 < self.cols and all(state[r][c+i] == p for i in range(4)):
                    return 1 if p == 'X' else -1
                if r + 3 < self.rows and all(state[r+i][c] == p for i in range(4)):
                    return 1 if p == 'X' else -1
                if r + 3 < self.rows and c + 3 < self.cols and all(state[r+i][c+i] == p for i in range(4)):
                    return 1 if p == 'X' else -1
                if r + 3 < self.rows and c - 3 >= 0 and all(state[r+i][c-i] == p for i in range(4)):
                    return 1 if p == 'X' else -1
        
        if all(state[0][c] != " " for c in range(self.cols)):
            return 0 # Draw
            
        return "Not terminal"

    def MinMax(self, state, depth):
        terminal = self.check_terminal(state)
        if terminal != "Not terminal" or depth == 0:
            return 0 if terminal == "Not terminal" else terminal

        possible_actions = self.available_actions(state)
        if not possible_actions: return 0

        values = []
        for action in possible_actions:
            next_state = self.take_action(state, action)
            values.append(self.MinMax(next_state, depth - 1))

        return max(values) if self.current_player(state) == 'X' else min(values)

    # Helper to get AI move 
    def get_ai_move(self, state):
        actions = self.available_actions(state)
        values = []
        for action in actions:
            next_state = self.take_action(state, action)
            values.append(self.MinMax(next_state, depth=4)) 

        player = self.current_player(state)
        best_val = max(values) if player == 'X' else min(values)
        index = values.index(best_val)
        return actions[index]


# --- TKINTER GUI CLASS ---
class Connect4GUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Connect 4 - AI (Red) vs Human (Yellow)")
        
        self.game = Connect_4()
        self.grid = [row[:] for row in self.game.initial_grid] # Deep copy initial grid
        self.game_over = False

       
        self.cell_size = 100
        self.width = self.game.cols * self.cell_size
        self.height = self.game.rows * self.cell_size
        
       
        self.canvas = tk.Canvas(root, width=self.width, height=self.height, bg='#0000FF')
        self.canvas.pack()
        
        
        self.canvas.bind("<Button-1>", self.handle_click)
        
        self.draw_board()
        
        
        if self.game.current_player(self.grid) == 'X':
            self.root.after(500, self.run_computer_move)

    def draw_board(self):
        self.canvas.delete("all")
        
        for r in range(self.game.rows):
            for c in range(self.game.cols):
                x0 = c * self.cell_size
                y0 = r * self.cell_size
                x1 = x0 + self.cell_size
                y1 = y0 + self.cell_size
                
                # Determine color based on grid state
                piece = self.grid[r][c]
                if piece == 'X':
                    color = 'red'
                elif piece == 'O':
                    color = 'yellow'
                else:
                    color = 'white' # Empty slot
                
                
                self.canvas.create_oval(x0 + 10, y0 + 10, x1 - 10, y1 - 10, fill=color, outline="black")

    def handle_click(self, event):
        if self.game_over:
            return

        if self.game.current_player(self.grid) != 'O':
            return

        col = event.x // self.cell_size
        
        # Check if column is valid (not full)
        if self.grid[0][col] != " ":
            return # Column is full
            
       
        self.grid = self.game.take_action(self.grid, ('O', col))
        self.draw_board()
        self.root.update() 
        
        if self.check_game_over():
            return
            
        
        self.root.config(cursor="watch")
        self.root.after(100, self.run_computer_move)

    def run_computer_move(self):
        if self.game_over: return
        
        # Get AI move
        action = self.game.get_ai_move(self.grid)
        self.grid = self.game.take_action(self.grid, action)
        
        self.draw_board()
        self.root.config(cursor="") # Reset cursor
        
        self.check_game_over()

    def check_game_over(self):
        result = self.game.check_terminal(self.grid)
        if result != "Not terminal":
            self.game_over = True
            msg = ""
            if result == 1:
                msg = "Computer (Red) Wins!"
            elif result == -1:
                msg = "You (Yellow) Win!"
            else:
                msg = "It's a Draw!"
            
            
            if messagebox.askyesno("Game Over", f"{msg}\nDo you want to play again?"):
                self.reset_game()
            else:
                self.root.quit()
            return True
        return False

    def reset_game(self):
        """Resets the game state and board."""
        self.game_over = False
        
        self.grid = [[" " for _ in range(self.game.cols)] for _ in range(self.game.rows)]
        self.draw_board()
        
       
        if self.game.current_player(self.grid) == 'X':
            self.root.after(500, self.run_computer_move)

# --- MAIN ---
if __name__ == "__main__":
    root = tk.Tk()
    app = Connect4GUI(root)
    root.mainloop()