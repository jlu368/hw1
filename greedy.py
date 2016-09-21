import math

def greedy(start, goal, max_steps):
    x = goal.x
    y = goal.y
    frontier = [(start, [start])]
    count = 0
    
    while frontier:
       # if count > max_steps:
        #    return []

        next, path = frontier.pop(0)
        if next == goal:
            return path

        if next.left and next.left not in path:
            next.left.manhattan = manhattan(next.left, goal)
            frontier = insert_sorted(frontier, next.left, path, 0, len(frontier))
        if next.top and next.top not in path:
            next.top.manhattan = manhattan(next.top, goal)
            frontier = insert_sorted(frontier, next.top, path, 0, len(frontier))
        if next.bottom and next.bottom not in path:
            next.bottom.manhattan = manhattan(next.bottom, goal)
            frontier = insert_sorted(frontier, next.bottom, path, 0, len(frontier))
        if next.right and next.right not in path:
            next.right.manhattan = manhattan(next.right, goal)
            frontier = insert_sorted(frontier, next.right, path, 0, len(frontier))
        print(len(frontier))
        #count += 1


def manhattan(node, goal):
    return math.fabs((goal.y - node.y)) + math.fabs((goal.x - node.x))

def insert_into(frontier, node, path):
    if not frontier or node.manhattan < frontier[0][0].manhattan:
        frontier.insert(0, (node, path + [node]))
        return frontier

    for i in range(1, len(frontier)):
        if frontier[i-1][0].manhattan <= node.manhattan and node.manhattan <= frontier[i][0].manhattan:
            frontier.insert(i, (node, path + [node]))
            return frontier

    frontier.append((node, path + [node]))
    return frontier

def insert_sorted(frontier, node, path, start, end):
    if end - start == 1:
        if frontier[start][0].manhattan >= node.manhattan:
            frontier.insert(start, (node, path + [node]))
        elif frontier[start][0].manhattan < node.manhattan:
            frontier.insert(end, (node, path + [node]))
        return frontier

    mid = (int)((start + end) / 2)
    if mid == start or frontier[mid][0].manhattan == node.manhattan:
        frontier.insert(mid, (node, path + [node]))
        return frontier

    if frontier[mid][0].manhattan > node.manhattan:
        return insert_sorted(frontier, node, path, start, mid-1)

    if frontier[mid][0].manhattan < node.manhattan:
        return insert_sorted(frontier, node, path, mid+1, end)
    


