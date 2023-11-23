import tkinter as tk

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("400x450")
        self.title("Chess")

        self.canvas = tk.Canvas(self, width=400, height=400, bg="white")
        self.canvas.pack()

        self.draw_board()

    def draw_board(self):
        for i in range(0, 8):
            for j in range(0, 8):
                x1 = 5 + 50 * i
                y1 = 5 + 50 * j
                x2 = x1 + 50
                y2 = y1 + 50
                if (i + j) % 2 == 0:
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill="white")
                else:
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill="gray")

if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()

def draw_white_pawn(self, x, y):
    x1 = 15 + 50 * x
    y1 = 15 + 50 * y
    x2 = x1 + 30
    y2 = y1 + 50
    self.canvas.create_polygon(x1, y1, x2, y1, x2 + 10, y2 - 10, x2 - 10, y2 - 10, fill="white")
def draw_black_pawn(self, x, y):
    x1 = 15 + 50 * x
    y1 = 15 + 50 * y
    x2 = x1 + 30
    y2 = y1 + 50
    self.canvas.create_polygon(x1, y1, x2, y1, x2 + 10, y2 + 10, x2 - 10, y2 + 10, fill="black")
def on_square_click(self, event):
    x = event.x // 50
    y = event.y // 50
    print(f"Clicked square at position ({x}, {y})")
    self.canvas.bind("<Button-1>", self.on_square_click)