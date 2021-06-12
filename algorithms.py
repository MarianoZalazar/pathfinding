import pygame
import queue
import math

        
def reconstruct_path(came_from, start, current, draw):
    #Reconstruct the path based in the END node
    #Uses a dictionary wich has a Node as key and the value is
    #the node where it has come from
    
    while (current in came_from) and current != start:
        current = came_from[current]
        current.make_path()
        draw()
        
        
        
        
        
        
#################### A* Algorithm

#Heuristic Function
def h(p1, p2):
    
    x1, y1 = p1
    x2, y2 = p2
    #Makes an assumption based in Manhattan Distance (good when working with grids)
    d = abs(x1 - x2) + abs(y1 - y2)
    
    #.............................Euclidean Distance
    #d = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
    
    return d

def a_star(draw, grid, start, end):
    #Setting Variables
    cont = 0
    came_from = {}
    
    ##A Priority Queue returns a value not based on the default FIFO
    ##it bases it on the 'Priority' of the value
    ##Python uses a Binary Heap Structure to do this, so every 'node'(value in this case)
    ##works as a unity with the other to relocate itself when other node is 'pushed' or 'popped'
    ##into the heap
    open_set = queue.PriorityQueue()
    
    ##We use a tuple, the first element is the value(here's the f_score) of priority
    ##the second values works as a tie-breaker in case two nodes have the same f_score
    ##and the third is the node itself
    open_set.put((0, cont, start))
    
    ##Define the value of every node's g_score/f_score to infinity, for initialization purposes 
    g_score = {node: float("inf") for row in grid for node in row}
    f_score = {node: float("inf") for row in grid for node in row}
    
    ##Set the values for the Start Node
    g_score[start] = 0
    f_score[start] = h(start.get_pos(), end.get_pos())
    
    ##We can't read a PriorityQueue so we use a hash like an aux
    open_set_hash = {start}
    
    
    while not open_set.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                
                pygame.quit()
                
        #Get the shortets value out of the PQ
        current = open_set.get()[2]
        open_set_hash.remove(current)
        
        #Checks if we made it to the End Node, draws the path and finishes the function
        if current == end:
            reconstruct_path(came_from, start, end, draw)
            start.make_start()
            end.make_end()
            return True
        
        for neighbor in current.neighbors:
            #Get the g_score of the current Node and add 1
            #If we were working with weighted nodes, we would be adding the weight of the neighbor
            #Because the 'weight' of every neighbor is always 1 we add that
            temp_g_score = g_score[current] + 1
            
            #Checks if the temp_g_score is less than the g_score of the neighbor
            #This value could be 'inf'(line 53) or another value if we visited it before hand
            if temp_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = temp_g_score
                f_score[neighbor] = temp_g_score + h(neighbor.get_pos(), end.get_pos())
                
                #Our not so important hash, takes relevance and makes a check
                #This is for a node with multiple neighbors
                if neighbor not in open_set_hash:
                    cont +=1
                    open_set.put((f_score[neighbor], cont, neighbor))
                    open_set_hash.add(neighbor)
                    neighbor.make_open()
        draw()
        
        if current != start:
            current.make_closed()
            
    return False

#################### Dijkstra Algorithm

def dijkstra(draw, grid, start, end):
    #Setting Variables
    cont = 0
    visited = {}
    
    ##A Priority Queue returns a value not based on the default FIFO
    ##it bases it on the 'Priority' of the value
    ##Python uses a Binary Heap Structure to do this, so every 'node'(value in this case)
    ##work as a unity with the others to relocate itself when other node is 'pushed' or 'popped'
    ##into the heap
    open_set = queue.PriorityQueue()
    
    ##We use a tuple, the first element is the value(here's the f_score) of priority
    ##the second values works as a tie-breaker in case two nodes have the same f_score
    ##and the third is the node itself
    open_set.put((0, cont, start))
    
    ##Define the value of every node's shortest_path to infinity, for initialization purposes 
    shortest_value = {node: float("inf") for row in grid for node in row}
    
    ##Set the values for the Start Node
    shortest_value[start] = 0
    
    ##We can't read a PriorityQueue, it will return a PriorityQueue object
    ##so we use a hash like an aux
    open_set_hash = {start}
    
    
    while not open_set.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                
        #Get the shortets value out of the PQ
        current = open_set.get()[2]
        open_set_hash.remove(current)
        
        #Checks if we made it to the End Node, draws the path and finishes the function
        if current == end:
            reconstruct_path(visited, start, end, draw)
            start.make_start()
            end.make_end()
            return True
        
        for neighbor in current.neighbors:
            temp_value = shortest_value[current] + 1
            
            #Checks if the temp_value is less than the shortest_value of the neighbor
            #This value could be 'inf'(line 41) or another value if we visited it before hand
            if temp_value < shortest_value[neighbor]:
                visited[neighbor] = current
                shortest_value[neighbor] = temp_value
                #Our not so important hash, takes relevance and makes a check
                #This is for a node with multiple neighbors
                if neighbor not in open_set_hash:
                    cont +=1
                    open_set.put((shortest_value[neighbor], cont, neighbor))
                    open_set_hash.add(neighbor)
                    neighbor.make_open()
        draw()
        
        if current != start:
            current.make_closed()
            
    return False


#################### Breadth First Search Algorithm

#This algorithm its not so useful when we're working with weighted edges
#because it just passes to the other node without thinking of its weight
def bfs(draw, grid, start, end):
    visited = {}
    
    #This algorithm besides Dijkstra and A_Star uses a Queue structure
    #This structure is based on a FIFO system
    #The only thing that matters here is the order of arrival
    moves = queue.Queue()
    moves.put(start)
    while not moves.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                
        current = moves.get()
        
        #Checks if we made it to the End Node, draws the path and finishes the function
        if current == end:
            reconstruct_path(visited, start, end, draw)
            start.make_start()
            end.make_end()
            return True
        
        for neighbor in current.neighbors:
            #We don't mind if the next neighbor is not an optimal choice
            #we just need to know if we've already visited it to avoid repeating ourselves
            if not neighbor.is_open():
                visited[neighbor] = current
                moves.put(neighbor)
                neighbor.make_open()
                
        if current == start:
            current.make_start()
        draw()
            
    return False
        

#################### Depth First Search Algorithm


#This algorithm won't give us the shortest path
#but its useful in decision tree situations
def dfs(draw, grid, start, end):
    visited = {}
    
    #This algorithm besides Breadth-First Search uses a Stack structure
    #This structure is based on a LIFO system
    #The only thing that matters here is the order of arrival
    moves = queue.LifoQueue()
    moves.put(start)
    while not moves.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                
        current = moves.get()
        
        #Checks if we made it to the End Node, draws the path and finishes the function
        if current == end:
            reconstruct_path(visited, start, end, draw)
            start.make_start()
            end.make_end()
            return True
        
        for neighbor in current.neighbors:
            #We don't mind if the next neighbor is not an optimal choice
            #we just need to know if we've already visited it to avoid repeating ourselves
            if not neighbor.is_open():
                visited[neighbor] = current
                moves.put(neighbor)
                neighbor.make_open()
                
        if current == start:
            current.make_start()
        draw()
            
    return False




