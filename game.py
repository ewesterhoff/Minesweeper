import random
import numpy

class Cell():
    """ Each cell in a minesweeper board """
    def __init__(self, is_mine, is_visible = False, is_visible = False):
        self.is_mine = is_mine
        self.is_visible = is_visible
        self.is_flagged = is_flagged

    def show(self):
        self.is_visible = True

    def flag(self):
        self.is_flagged = True

    def place_mine(self):
        self.is_mine = True

class Board():
    """ Player board """
    def __init__(self, is_playing, dim, num_mines):
        self.is_playing = is_playing
        self.dim = dim
        self.num_mines = num_mines

        for a in range(dim):
            for b in range(dim):
                #calculate probability of this one being a mine
                is_mine = False
                grid[a,b] = Cell(is_mine)

    def show(self):


if __name__ == "__main__":
    board = Board(True, 8, 10)

    while board.is_playing = True:
        board.show()
