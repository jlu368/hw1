import IPython

class Node():
	top = None
	bottom = None
	left = None
	right = None
	wall = False
	point = False

def main():
	content = None
	with open('medium_maze.txt') as f:
		content = f.readlines()

	content = [x.strip('\n') for x in content]
	maze = []
	temp_arr = []
	start = None

	for i in range(0, len(content[0])):
		temp_node = Node()
		temp_node.wall = True
		temp_arr.append(temp_node)
	maze.append(temp_arr.copy())
	for x in range(1, len(content) - 1):
		maze.append([])
		for i in range(0, len(content[x])):
			node, maze = check_node(maze, content, x, i)
			maze[x].append(node)

def check_node(maze, content, x, i):
	temp_node = Node()
	if content[x][i] == '%':
		temp_node.wall = True
	else:
		top = maze[x-1][i]
		left = maze[x][i-1]
		if not top.wall:
			temp_node.top = top
			top.bottom = temp_node
		if not left.wall:
			temp_node.left = left
			left.right = temp_node
		if content[x][i] == '.':
			temp_node.point = True
		elif content[x][i] == 'P':
			start = temp_node
	return temp_node, maze

main()
	
