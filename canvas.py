# This program creates a grid of blue squares and allows the user to erase them
# by moving a pink eraser around the canvas. The eraser will erase any blue squares it touches.
# The program uses the tkinter library to create a GUI window and handle mouse events.
# The canvas is created with a specified width and height, and the squares are drawn in a grid pattern.
import tkinter as tk
import time

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
CELL_SIZE = 40
ERASER_SIZE = 20

class EraserApp:
    def __init__(self, root):
        self.canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg='white')
        self.canvas.pack()
        self.grid_cells = []

        self.create_grid()

        self.eraser = None
        self.canvas.bind("<Button-1>", self.start_eraser)

    def create_grid(self):
        for row in range(0, CANVAS_HEIGHT, CELL_SIZE):
            for col in range(0, CANVAS_WIDTH, CELL_SIZE):
                rect = self.canvas.create_rectangle(
                    col, row, col + CELL_SIZE, row + CELL_SIZE,
                    fill='blue', outline='black'
                )
                self.grid_cells.append(rect)

    def start_eraser(self, event):
        self.eraser = self.canvas.create_rectangle(
            event.x, event.y, event.x + ERASER_SIZE, event.y + ERASER_SIZE,
            fill='pink'
        )
        self.canvas.bind("<Motion>", self.move_eraser)

    def move_eraser(self, event):
        if self.eraser:
            self.canvas.coords(
                self.eraser,
                event.x, event.y,
                event.x + ERASER_SIZE, event.y + ERASER_SIZE
            )
            self.erase(event.x, event.y)

    def erase(self, x, y):
        items = self.canvas.find_overlapping(x, y, x + ERASER_SIZE, y + ERASER_SIZE)
        for item in items:
            if item != self.eraser:
                self.canvas.itemconfig(item, fill='white')

if __name__ == '__main__':
    root = tk.Tk()
    root.title("Eraser App")
    app = EraserApp(root)
    root.mainloop()
# This program creates a grid of blue squares and allows the user to erase them