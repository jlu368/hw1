from queue import Queue

def bfs(start):
    queue = Queue()
    queue.put((start, [start]))

    while not queue.empty():
        node, path = queue.get()
        if node.point:
            return path

        if node.left and node.left not in path:
            queue.put((node.left, path + [node.left]))
        if node.top and node.top not in path:
            queue.put((node.top, path + [node.top]))
        if node.right and node.right not in path:
            queue.put((node.right, path + [node.right]))
        if node.bottom and node.bottom not in path:
            queue.put((node.bottom, path + [node.bottom]))
