import math

class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
    	if len(self.items) == 0:
    		self.items.insert(0, item)
    		return
    	for i in range((len(self.items))):
    		if item[0] <= self.items[i][0]:
    			self.items.insert(i, item)
    			return 
    	self.items.insert(len(self.items), item)

    def printqueue(self):
	    return self.items

    def frontenqueue(self, item):
    	self.items.insert(len(self.items), item)

    def dequeue(self):
    	temp = self.items[0]
    	del self.items[0]
    	return temp

    def size(self):
	    return len(self.items)

def astar(start, goal):
	counter = 0
	openset = set() #set.remove(), set.add()
	closedset = set()
	path = []
	dict = {} #Corresponding coordinates key:coord -> value:f
	q = Queue()
	q.enqueue((manhat(start, goal), start))
	dict[(start.y, start.x)] = (manhat(start, goal))
	openset.add(start)
	while openset:
		#counter = counter + 1
		#print(counter)
		curr = q.dequeue()
		currdist = curr[0]
		currnode = curr[1]
		print(currnode.y, currnode.x)
		if currnode in openset:
			openset.remove(currnode)
		temp = []
		if currnode.left:
			temp.append(currnode.left)
		if currnode.right:
			temp.append(currnode.right)
		if currnode.top:
			temp.append(currnode.top)
		if currnode.bottom:
			temp.append(currnode.bottom)
		for i in temp:
			if i.point:
				print("Find the goal!")
				break
			succ_g = 1 + currdist - manhat(currnode, goal)
			succ_h = manhat(i, goal)
			succ_f = succ_g + succ_h
			if (i.y, i.x) not in dict:
				dict[(i.y, i.x)] = succ_f
			#print(succ_f)
			if i in openset and (succ_f > dict[(i.y, i.x)]):
				continue
			if i in closedset and (succ_f > dict[(i.y, i.x)]):
				continue
		    
			openset.add(i)
			dict[(i.y, i.x)] = succ_f
			q.enqueue((succ_f, i))
		closedset.add(currnode)
		path.append(currnode)
	return path


def manhat(node, goal):
	return math.fabs(node.y - goal.y) + math.fabs(node.x - goal.x)

# // A*
# initialize the open list
# initialize the closed list
# put the starting node on the open list (you can leave its f at zero)

# while the open list is not empty
#     find the node with the least f on the open list, call it "q"
#     pop q off the open list
#     generate q's 4 successors and set their parents to q
#     for each successor
#     	if successor is the goal, stop the search
#         successor.g = q.g + distance between successor and q
#         successor.h = distance from goal to successor
#         successor.f = successor.g + successor.h

#         if a node with the same position as successor is in the OPEN list \
#             which has a lower f than successor, skip this successor
#         if a node with the same position as successor is in the CLOSED list \ 
#             which has a lower f than successor, skip this successor
#         otherwise, add the node to the open list
#     end
#     push q on the closed list
# end

			



