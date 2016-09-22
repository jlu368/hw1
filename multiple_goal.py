import newstar, heapq

def mult(start, goals):
	start_edges = []
	goal_edges = []
	visited = set()
	for goal in goals:
		path = astar(start, goal)
		heapq.heappush(start_edges, (len(path), path))

	for goal1 in goals:
		visited.add(goal1)
		for goal2 in goals and goal2 not in visited:
			path = astar(goal1, goal2)
			heapq.heappush(goal_edges, (len(path), path))

	start_edges.extend(goal_edges)
