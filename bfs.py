from queue import Queue, LifoQueue

def bfs(start): # Implementation of BFS search algorithm
    queue = Queue()  # Using queue structure 
    queue.put((start, [start]))
    expansion = 0
    visited = set() # Frontier to keep track of nodes that have been visited
                    # Prevent repeated state 

    while not queue.empty():
        node, path = queue.get()
        expansion += 1
        if node.point: # If the current node is goal, return
            print("BFS Expansion: ", expansion)
            return path
        # Traverse and en-queue the fours neighbors of current nodes 
        if node.left and node.left not in path and node.left not in visited:
            queue.put((node.left, path + [node.left]))
            visited.add(node.left)
        if node.top and node.top not in path and node.top not in visited:
            queue.put((node.top, path + [node.top]))
            visited.add(node.top)
        if node.right and node.right not in path and node.right not in visited:
            queue.put((node.right, path + [node.right]))
            visited.add(node.right)
        if node.bottom and node.bottom not in path and node.bottom not in visited:
            queue.put((node.bottom, path + [node.bottom]))
            visited.add(node.bottom)

def dfs(start):  #Implementation of DFS search algorithm
    stack = LifoQueue()  # Using stack structure 
    stack.put((start, [start]))
    expansion = 0
    visited = set() # Frontier to keep track of nodes that have been visited
                    # Prevent repeated state 

    while not stack.empty():
        node, path = stack.get()
        expansion += 1
        if node.point: # If the current node is goal, return
            print("DFS Expansion: ", expansion)
            return path
        # Traverse and en-queue the fours neighbors of current nodes 
        if node.left and node.left not in path and node.left not in visited:
            stack.put((node.left, path + [node.left]))
            visited.add(node.left)
        if node.top and node.top not in path and node.top not in visited:
            stack.put((node.top, path + [node.top]))
            visited.add(node.top)
        if node.right and node.right not in path and node.right not in visited:
            stack.put((node.right, path + [node.right]))
            visited.add(node.right)
        if node.bottom and node.bottom not in path and node.bottom not in visited:
            stack.put((node.bottom, path + [node.bottom]))
            visited.add(node.bottom)
