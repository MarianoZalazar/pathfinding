import pygame

GRID_COLOR = (108, 117, 125)
START_COLOR = (20, 70, 160)
END_COLOR = (219, 48, 105)
WHITE = (255, 255, 255)
PATH_COLOR = (64,224,208)
OBS_COLOR = (60, 60, 59)
CLOSED_COLOR = (154, 252, 190)
OPEN_COLOR = (24, 255, 109)

class Node:
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.x = width * row
        self.y = col * width
        self.color = WHITE
        self.neighbors = []
        self.width = width
        self.total_rows = total_rows
        
    def get_pos(self):
        return self.row, self.col
    
    def is_closed(self):
        return self.color == CLOSED_COLOR
    
    def is_open(self):
        return self.color == OPEN_COLOR
    
    def is_obstacle(self):
        return self.color == OBS_COLOR
    
    def is_start(self):
        return self.color == START_COLOR
    
    def is_end(self):
        return self.color == END_COLOR

    def is_path(self):
        return self.color == PATH_COLOR
    
    def reset(self):
        self.color = WHITE
        
    def make_start(self):
        self.color = START_COLOR
        
    def make_open(self):
        self.color = OPEN_COLOR
    
    def make_closed(self):
        self.color = CLOSED_COLOR
        
    def make_obstacle(self):
        self.color = OBS_COLOR
    
    def make_end(self):
        self.color = END_COLOR
    
    def make_path(self):
        self.color = PATH_COLOR
        
    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))
    
    def update_neighbors(self, grid):
        self.neighbors = []
        #Check for every possible neighbor that's not an obstacle and if it's in the boundaries of our grid
        if self.row < self.total_rows - 1 and not grid[self.row + 1][self.col].is_obstacle(): #DOWN
            self.neighbors.append(grid[self.row + 1][self.col])
            
        if self.row > 0 and not grid[self.row - 1][self.col].is_obstacle(): #UP
            self.neighbors.append(grid[self.row - 1][self.col])
            
        if self.col < self.total_rows - 1 and not grid[self.row][self.col + 1].is_obstacle(): #RIGHT
            self.neighbors.append(grid[self.row][self.col + 1])
            
        if self.col > 0 and not grid[self.row][self.col - 1].is_obstacle(): #LEFT
            self.neighbors.append(grid[self.row][self.col - 1])
            
    #search lt class
    def __lt__(self, other):
        return False