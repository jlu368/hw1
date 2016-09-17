import bfs, greedy

class Node():
    top = None
    bottom = None
    left = None
    right = None
    wall = False
    point = False
    x = -1
    y = -1
    manhattan = 0

    def __lt__(self, other):
        return self.manhattan < other.manhattan

    def __gt__(self, other):
        return self.manhattan > other.manhattan        

def main():
    with open('open_maze.txt') as f:
        content = f.readlines()

    content = [x.strip('\n') for x in content]
    maze = []
    temp_arr = []
    start = None
    goal = None

    for i in range(0, len(content[0])):
        temp_node = Node()
        temp_node.wall = True
        temp_node.x = i
        temp_node.y = 0
        temp_arr.append(temp_node)
    maze.append(temp_arr.copy())
    for y in range(1, len(content) - 1):
        maze.append([])
        for x in range(0, len(content[y])):
            node, maze = check_node(maze, content, y, x)
            maze[y].append(node)
            if content[y][x] == 'P':
                start = node
            if content[y][x] == '.':
                goal = node

    maze.append(temp_arr.copy())

    result = greedy.greedy(start, goal, 0)
    
    print_maze(maze, result, start)

def print_maze(maze, result, start):
    for row in maze:
        for point in row:
            if point.wall:
                print('%', end="", flush=True)
            elif point == start:
                print('P', end="", flush=True)
            elif point.point or point in result:
                print('.', end="", flush=True)
            else:
                print(' ', end="", flush=True)
        print()


def check_node(maze, content, y, x):
    temp_node = Node()
    if content[y][x] == '%':
        temp_node.wall = True
    else:
        top = maze[y-1][x]
        left = maze[y][x-1]
        if not top.wall:
            temp_node.top = top
            top.bottom = temp_node
        if not left.wall:
            temp_node.left = left
            left.right = temp_node
        if content[y][x] == '.':
            temp_node.point = True
    temp_node.x = x
    temp_node.y = y

    return temp_node, maze

main()
	
