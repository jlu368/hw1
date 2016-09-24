import newstar, heapq, copy

def mult(start, goals):
    start_edges = []
    goal_edges = []
    for goal in goals:
        path = newstar.astar(start, goal)
        heapq.heappush(start_edges, (len(path), path))

    for goal1 in goals:
        goals.remove(goal1)
        for goal2 in goals:
            path = newstar.astar(goal1, goal2)
            heapq.heappush(goal_edges, (len(path), path))

    sep_goals = separate(goals)
    goal_mst = mst(goal_edges, sep_goals)

def separate(goals):
    result = []
    for goal in goals:
        result.append([goal])
    return result

def findset(node, goals):
    for i in range(0, len(goals)):
        if node in goals[i]:
            return i

def union(node1, node2, goals):
    for node in goals[node2]:
        goals[node1].append(node)
    goals.remove(goals[node2])

def mst(edges, goals):
    mst_edges = []
    for edge in edges:
        start_idx = findset(edge[1][0], goals)
        end_idx = findset(edge[1][-1], goals)
        if start_idx != end_idx:
            union(start_idx, end_idx, goals)
            mst_edges.append(edge)

# def mult(start, goals):
#     openset = set()
#     opendict = {}
#     closeset = set()
#     front = []
#     heapq.heappush(front, ((manhat_all(start, closeset, goals), start),
#         [start], copy.copy(goals), []))
#     openset.add(start)
#     opendict[start] = 0
#     while not openset == None:
#         currtuple = heapq.heappop(front)
#         curr = currtuple[0][1]
#         currheur = currtuple[0][0]
#         currpath = currtuple[1]
#         currgoals = currtuple[2]
#         print(openset, ' ', closeset)
#         if curr.point:
#             currgoals.remove(curr)
#             currtuple[3].append((curr.y, curr.x))
#             if not currgoals:
#                 return currpath, currtuple[3]
#
#         temp = []
#         if curr.left:
#             temp.append(curr.left)
#         if curr.right:
#             temp.append(curr.right)
#         if curr.top:
#             temp.append(curr.top)
#         if curr.bottom:
#             temp.append(curr.bottom)
#         for i in temp:
#             # succ_g = currheur - manhat_all(curr, closeset, currgoals) + 1
#             temp_heur = manhat_all(i, closeset, currgoals)
#
#             if i in closeset:
#                 if temp_heur > currheur:
#                     continue
#                 closeset.remove(i)
#                 openset.add(i)
#             elif i in openset:
#                 if temp_heur > currheur:
#                     continue
#             else:
#                 openset.add(i)
#                 # succ_h = succ_g + manhat_all(i, closeset, currgoals)
#                 heapq.heappush(front, ((temp_heur, i), copy.copy(currpath + [i]),
#                                        copy.copy(currgoals), copy.copy(currtuple[3])))
#
#     # opendict[i] = succ_g
#         closeset.add(curr)
#
# def manhat_all(node, closeset, goals):
# 	total = 0
# 	for goal in goals:
# 		if goal not in closeset and goal is not node:
# 			total += newstar.manhat(node, goal)
#
# 	return total
