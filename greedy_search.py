import math, heapq
# Implementation of greedy algorithm (Complete)
# This implementation of greedy does not guarantee to find an optimal solution, 
# but it is complete.
def greedy(start, goal):
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
		if curr.point:
			print("Greedy: ", expansion+1)
			return currpath

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
			succ_h = manhat(curr, goal)
			if i in openset:
				if succ_h > opendict[i]:
					continue
			elif i in closeset:
				if succ_h > opendict[i]:
					continue
				closeset.remove(i)
				openset.add(i)
			else:
				openset.add(i)
				heapq.heappush(front, ((succ_h, i), currpath + [i]))
			opendict[i] = succ_h
		closeset.add(curr)
		expansion += 1
		



def manhat(node, goal):
	return math.fabs(node.y - goal.y) + math.fabs(node.x - goal.x)
