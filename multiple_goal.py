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
	heapq.heappush(front, ((manhat_all(start, closeset, goals), start), 
		[start], goals, []))
	openset.add(start)
	opendict[start] = 0
	while not openset == None:
		currtuple = heapq.heappop(front)
		curr = currtuple[0][1]
		currheur = currtuple[0][0]
		currpath = currtuple[1]
		currgoals = currtuple[2]
		# print(currgoals)
		if curr.point:
			currgoals.remove(curr)
			currtuple[3].append((curr.y, curr.x))
			if not currgoals:
				return currpath, currtuple[3]
			
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
			# succ_g = currheur - manhat_all(curr, closeset, currgoals) + 1
			temp_heur = manhat_all(i, closeset, currgoals)
			if i in openset:
				if temp_heur > currheur:
					continue
			elif i in closeset:
				if temp_heur > currheur:
					continue
				closeset.remove(i)
				openset.add(i)
			else:
				openset.add(i)
				# succ_h = succ_g + manhat_all(i, closeset, currgoals)
				heapq.heappush(front, ((temp_heur, i), currpath + [i], 
					currgoals, currtuple[3]))

			# opendict[i] = succ_g
		closeset.add(curr)

def manhat_all(node, closeset, goals):
	total = 0
	for goal in goals:
		if goal not in closeset and goal is not node:
			total += newstar.manhat(node, goal)

	return total
