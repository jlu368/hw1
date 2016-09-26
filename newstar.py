import math, heapq

# In this a star search implentation, we used manhattan distance to determine 
# the heuristic value. Since in this case, Manhattan distance is the closest path 
# cost from current node to goal (Diagonal is not allowed), we can conclude that 
# our heuristic function never overestimate the true cost, and therefore, this 
# implementation is admissible. 

def astar(start, goal):
	openset = set() # Openset is a set that contains all the visited but not necessarily expanded nodes
	opendict = {}
	closeset = set() # Closedset is a set that contains all the visited and expanded nodes
	front = []
	heapq.heappush(front, ((manhat(start, goal), start), [start]))
	openset.add(start)
	opendict[start] = 0
	expansion = 0
	while not openset == None:
		currtuple = heapq.heappop(front) # Pop the node with the lowest total f cost off the heapqueue
										 # Where f = g(path cost) + h(heuristic cost) 
		curr = currtuple[0][1]
		currheur = currtuple[0][0]
		currpath = currtuple[1]
		if curr == goal:
			# print("A*: ", expansion+1)
			return currpath, expansion + 1 # The path cost between current state and next state is always 1

		temp = [] # Traverse the fours neighbors of current nodes 
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
			if i in openset: # If the current location has aleadys been visited 
							 # and its previous total cost is lower, do nothing
				if succ_g > opendict[i]:
					continue
			elif i in closeset: # If the current location has aleadys been visited and expanded
							    # and its previous total cost is lower, do nothing
				if succ_g > opendict[i]:
					continue
				closeset.remove(i)  # Otherwise, we need to pop it from closed set 
									# because its total cost is not optimal
				openset.add(i)
			else:
				openset.add(i)
				succ_h = succ_g + manhat(i, goal)
				heapq.heappush(front, ((succ_h, i), currpath + [i]))
			opendict[i] = succ_g
		closeset.add(curr) # Otherwise, we set current node as visted and expanded
		expansion += 1
		



def manhat(node, goal): # We use Manhattan distance as our heruistic function, 	
						# since it never overestimates the true cost, it is admissible
	return math.fabs(node.y - goal.y) + math.fabs(node.x - goal.x)

