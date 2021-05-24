import classes
import pygame
import mazes

WIDTH = 600
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption('Pathfinding Algorithm')

def get_maze(grid, width, rows, num):
    maze = mazes.maze1[num-1]
    grid = []
    gap = width // rows
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            node = classes.Node(i, j, gap, rows)
            if maze[i][j] == '#':
                node.make_obstacle()
            grid[i].append(node)
    return grid
    


def get_grid(grid, rows):
    new_grid = []
    for i in range(rows):
        new_grid.append([])
        for j in range(rows):
            node = grid[i][j]
            if node.is_obstacle():
                new_grid[i].append('#')
            else:
                new_grid[i].append('-')
    print(new_grid)
                

def clean_grid(grid, rows):
    for i in range(rows):
        for j in range(rows):
            node = grid[i][j]
            if node.is_open() or node.is_closed() or node.is_path():
                node.reset()
                
def clean_obstacles(grid, rows):
    for i in range(rows):
        for j in range(rows):
            node = grid[i][j]
            if node.is_obstacle():
                node.reset()
    clean_grid(grid, rows)

def make_grid(rows, width):
    grid = []
    gap = width // rows
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            node = classes.Node(i, j, gap, rows)
            grid[i].append(node)
            
    return grid

def draw_grid(win, rows, width):
    gap = width // rows
    for i in range(rows):
        pygame.draw.line(win, classes.GRID_COLOR, (0, i * gap), (width, i*gap))
    for j in range(rows):
        pygame.draw.line(win, classes.GRID_COLOR, (j*gap, 0), (j*gap, width))
        
def draw(win, grid, rows, width):
    win.fill(classes.WHITE)
    for row in grid:
        for node in row:
            node.draw(win)
    draw_grid(win, rows, width)
    pygame.display.update()
    
def get_clicked_pos(pos, rows, width):
    gap = width // rows
    i, j = pos
    row = i // gap
    col = j // gap
    return row, col
