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
	while not openset == None:
		currtuple = heapq.heappop(front)
		curr = currtuple[0][1]
		currheur = currtuple[0][0]
		currpath = currtuple[1]
		if curr.point:
			return currpath
			break
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
		



def manhat(node, goal):
	return math.fabs(node.y - goal.y) + math.fabs(node.x - goal.x)

			
# def astar(start, goal):
# 	counter = 0
# 	openset = set() #set.remove(), set.add()
# 	closedset = set()
# 	path = []
# 	dict = {} #Corresponding coordinates key:coord -> value:f
# 	q = Queue()
# 	q.enqueue((manhat(start, goal), start))
# 	dict[(start.y, start.x)] = (manhat(start, goal))
# 	openset.add(start)
# 	while openset:
# 		#counter = counter + 1
# 		#print(counter)
# 		curr = q.dequeue()
# 		currdist = curr[0]
# 		currnode = curr[1]
# 		print(currnode.y, currnode.x)
# 		if currnode in openset:
# 			openset.remove(currnode)
# 		temp = []
# 		if currnode.left:
# 			temp.append(currnode.left)
# 		if currnode.right:
# 			temp.append(currnode.right)
# 		if currnode.top:
# 			temp.append(currnode.top)
# 		if currnode.bottom:
# 			temp.append(currnode.bottom)
# 		for i in temp:
# 			if i.point:
# 				print("Find the goal!")
# 				break
# 			succ_g = 1 + currdist - manhat(currnode, goal)
# 			succ_h = manhat(i, goal)
# 			succ_f = succ_g + succ_h
# 			if (i.y, i.x) not in dict:
# 				dict[(i.y, i.x)] = succ_f
# 			#print(succ_f)
# 			if i in openset and (succ_f > dict[(i.y, i.x)]):
# 				continue
# 			if i in closedset and (succ_f > dict[(i.y, i.x)]):
# 				continue
		    
# 			openset.add(i)
# 			dict[(i.y, i.x)] = succ_f
# 			q.enqueue((succ_f, i))
# 		closedset.add(currnode)
# 		path.append(currnode)
# 	return path

