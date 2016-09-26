import math, heapq
# Implementation of greedy algorithm (Complete)
# This implementation of greedy does not guarantee to find an optimal solution, 
# but it is complete.
def greedy(start, goal):
	openset = set() # Openset is a set that contains all the visited but not necessarily expanded nodes 
	opendict = {}
	closeset = set() # Closedset is a set that contains all the visited and expanded nodes
	front = []
	heapq.heappush(front, ((manhat(start, goal), start), [start]))
	openset.add(start)
	opendict[start] = 0
	expansion = 0
	while not openset == None: 
		currtuple = heapq.heappop(front) # Pop the node with the lowest heruistic value off the heapqueue
		curr = currtuple[0][1]
		currheur = currtuple[0][0]
		currpath = currtuple[1]
		if curr.point:  # If the current node is goal, return
			print("Greedy: ", expansion+1)
			return currpath

		temp = []  # Traverse the fours neighbors of current nodes 
		if curr.left:
			temp.append(curr.left)
		if curr.right:
			temp.append(curr.right)
		if curr.top:
			temp.append(curr.top)
		if curr.bottom:
			temp.append(curr.bottom)
		for i in temp:
			succ_h = manhat(curr, goal)
			if i in openset: # If the current location has aleadys been visited 
							 # and its previous heuristic value is lower, do nothing
				if succ_h > opendict[i]:
					continue
			elif i in closeset: # If the current location has aleadys been visited and expanded
							    # and its previous heuristic value is lower, do nothing
				if succ_h > opendict[i]:
					continue
				closeset.remove(i)  # Otherwise, we need to pop it from closed set 
									# because its heuristic value is not optimal
				openset.add(i)
			else:
				openset.add(i)
				heapq.heappush(front, ((succ_h, i), currpath + [i]))
			opendict[i] = succ_h
		closeset.add(curr) # Otherwise, we set current node as visted and expanded
		expansion += 1
		



def manhat(node, goal):
	return math.fabs(node.y - goal.y) + math.fabs(node.x - goal.x)
