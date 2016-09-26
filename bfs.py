from queue import Queue, LifoQueue

def bfs(start):
    queue = Queue()
    queue.put((start, [start]))
    expansion = 0
    visited = set()

    while not queue.empty():
        node, path = queue.get()
        expansion += 1
        if node.point:
            print("BFS Expansion: ", expansion)
            return path

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

def dfs(start):
    stack = LifoQueue()
    stack.put((start, [start]))
    expansion = 0
    visited = set()

    while not stack.empty():
        node, path = stack.get()
        expansion += 1
        if node.point:
            print("DFS Expansion: ", expansion)
            return path

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
