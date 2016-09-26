import math, heapq

# In this a star search implentation, we used manhattan distance to determine 
# the heuristic value. Since in this case, Manhattan distance is the closest path 
# cost from current node to goal (Diagonal is not allowed), we can conclude that 
# our heuristic function never overestimate the true cost, and therefore, this 
# implementation is admissible. 

def astar(start, goal):
	openset = set()
	opendict = {}
	closeset = set()
	front = []
	heapq.heappush(front, ((manhat(start, goal), start), [start]))
	openset.add(start)
	opendict[start] = 0
	expansion = 0
	while not openset == None:
		currtuple = heapq.heappop(front)
		curr = currtuple[0][1]
		currheur = currtuple[0][0]
		currpath = currtuple[1]
		if curr == goal:
			# print("A*: ", expansion+1)
			return currpath, expansion + 1

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
			succ_g = currheur - manhat(curr, goal) + 1
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
				succ_h = succ_g + manhat(i, goal)
				heapq.heappush(front, ((succ_h, i), currpath + [i]))
			opendict[i] = succ_g
		closeset.add(curr)
		expansion += 1
		



def manhat(node, goal):
	return math.fabs(node.y - goal.y) + math.fabs(node.x - goal.x)

