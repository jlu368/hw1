import bfs, astar_search, greedy_search, newstar, multiple_goal, sys

from string import ascii_letters


class Node():
    top = None
    bottom = None
    left = None
    right = None
    wall = False
    point = False
    x = -1
    y = -1
    order = None
    manhattan = 0

    def __repr__(self):
        return"({0}, {1})".format(self.y, self.x)

    def __lt__(self, other):
        return self.manhattan < other.manhattan

    def __gt__(self, other):
        return self.manhattan > other.manhattan        

def main():
    if len(sys.argv) > 1:
        arg = sys.argv[1]
    else:
        arg = 0
    with open('tinySearch.txt') as f:
        content = f.readlines()

    content = [x.strip('\n') for x in content]
    maze = []
    temp_arr = []
    start = None
    if arg == "2":
        goal = []
    else:
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
                if arg == "2":
                    goal.append(node)
                else:
                    goal = node

    maze.append(temp_arr.copy())

    #result = bfs.bfs(start, goal)
    #result = greedy_search.greedy(start, goal)
    #result = newstar.astar(start, goal)
    result, coords = multiple_goal.mult(start, goal)
    import IPython
    IPython.embed()

    print_maze(maze, result, start, coords)


def print_maze(maze, result, start, coords):
    for row in maze:
        for point in row:
            if point.wall:
                print('%', end="", flush=True)
            elif point == start:
                print('P', end="", flush=True)
            elif point in result:
                if point.point:
                    print(character(coords.index((point.y, point.x))), end="", flush=True)
                else:
                    print('.', end="", flush=True)
            else:
                print(' ', end="", flush=True)
        print()

def character(index):
    if index < 10:
        return index
    else:
        return ascii_letters[index - 10]


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
	
