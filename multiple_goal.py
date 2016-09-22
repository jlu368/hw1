import newstar, heapq

# def mult(start, goals):
# 	start_edges = []
# 	goal_edges = []
# 	visited = set()
# 	for goal in goals:
# 		path = newstar.astar(start, goal)
# 		heapq.heappush(start_edges, (len(path), path))

# 	for goal1 in goals:
# 		goals.remove(goal1)
# 		for goal2 in goals:
# 			path = newstar.astar(goal1, goal2)
# 			heapq.heappush(goal_edges, (len(path), path))

# 	smallest = None
# 	for node in start_edges:
# 		smallest = mst(node, smallest)

def mult(start, goals):
	openset = set()
	opendict = {}
	closeset = set()
	front = []
	heapq.heappush(front, ((manhat_all(start, closeset, goals), start), [start]))
	openset.add(start)
	opendict[start] = 0
	paths = []
	coords = []
	while not openset == None:
		currtuple = heapq.heappop(front)
		curr = currtuple[0][1]
		currheur = currtuple[0][0]
		currpath = currtuple[1]
		if curr.point:
			goals.remove(curr)
			paths.extend(currpath)
			coords.append((curr.y, curr.x))
			if not goals:
				return paths, coords
			
		temp = []
		if curr.left:
			temp.append(curr.left)
		if curr.right:
			temp.append(curr.right)
		if curr.top:
			temp.append(curr.top)
		if curr.bottom:
			temp.append(curr.bottom)
		for i in temp:
			succ_g = currheur - manhat_all(curr, closeset, goals) + 1
			if i in openset:
				if succ_g > opendict[i]:
					continue
			elif i in closeset:
				if succ_g > opendict[i]:
					continue
				closeset.remove(i)
				openset.add(i)
			else:
				openset.add(i)
				succ_h = succ_g + manhat_all(i, closeset, goals)
				heapq.heappush(front, ((succ_h, i), currpath + [i]))

			opendict[i] = succ_g
		closeset.add(curr)

def manhat_all(node, closeset, goals):
	total = 0
	for goal in goals:
		if goal not in closeset and goal is not node:
			total += newstar.manhat(node, goal)

	return total