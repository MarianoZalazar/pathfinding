import pygame
import visualization as v
import algorithms as algorithm 

def clean_grid(rows, width, start, end):
    start = None
    end = None
    grid = v.make_grid(rows, width)
    return start, end, grid


def main(win, width):
    rows = 15
    grid = v.make_grid(rows, width)
    
    start = None
    end = None
    
    run = True
    
    while run:
        v.draw(win, grid, rows, width)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                row, col = v.get_clicked_pos(pos, rows, width)
                node = grid[row][col]
                if not start and node != end:
                    start = node
                    start.make_start()
                elif not end and node != start:
                    end = node
                    end.make_end()
                elif node != end and node != start:
                    node.make_obstacle()
                
            elif pygame.mouse.get_pressed()[2]:
                pos = pygame.mouse.get_pos()
                row, col = v.get_clicked_pos(pos, rows, width)
                node = grid[row][col]
                if node == start:
                    start = None
                elif node == end:
                    end = None
                node.reset()
                
            if event.type == pygame.KEYDOWN:
                
                #Use 'h' for A-star algorithm  
                if event.key == pygame.K_h and start and end:
                    v.clean_grid(grid, rows)
                    for row in grid:
                        for node in row:
                            node.update_neighbors(grid)
                    algorithm.a_star(lambda: v.draw(win, grid, rows, width), grid, start, end)
                
                #Use 'j' for Dijkstra algorithm  
                if event.key == pygame.K_j and start and end:
                    v.clean_grid(grid, rows)
                    for row in grid:
                        for node in row:
                            node.update_neighbors(grid)
                    algorithm.dijkstra(lambda: v.draw(win, grid, rows, width), grid, start, end)
                
                #Use 'k' for BFS algorithm  
                if event.key == pygame.K_k and start and end:
                    v.clean_grid(grid, rows)
                    for row in grid:
                        for node in row:
                            node.update_neighbors(grid)
                    algorithm.bfs(lambda: v.draw(win, grid, rows, width), grid, start, end)
                
                #Use 'l' for DFS algorithm  
                if event.key == pygame.K_l and start and end:
                    v.clean_grid(grid, rows)
                    for row in grid:
                        for node in row:
                            node.update_neighbors(grid)
                    algorithm.dfs(lambda: v.draw(win, grid, rows, width), grid, start, end)
                
                
                #Use '1' for maze 1  
                if event.key == pygame.K_1:
                    grid = v.get_maze(grid, width, rows, 1)
                    start = None 
                    end = None
                
                #Use '2' for maze 2    
                if event.key == pygame.K_2:
                    grid = v.get_maze(grid, width, rows, 2)
                    start = None
                    end = None
                
                #Use '3' for maze 3    
                if event.key == pygame.K_3:
                    grid = v.get_maze(grid, width, rows, 3)
                    start = None
                    end = None
                
                #Use 'c' to clean everything
                if event.key == pygame.K_c:
                    v.clean_grid(grid, rows)

                #Use 'v' to clean only obstacles
                if event.key == pygame.K_v:
                    v.clean_obstacles(grid, rows)
    pygame.quit()


main(v.WIN, v.WIDTH)