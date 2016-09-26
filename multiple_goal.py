import newstar, heapq
from queue import LifoQueue

# This function starts the process of solving a maze for multiple dots.
# Params:
#   start - Node that signifies the starting position in the maze
#   goals - Array of nodes that are all goal states
#
# Returns:
#   The solution to the maze as an array of nodes, and the order of the goals accessed by coordinates
def mult(start, goals):
    goal_edges = []     # List of all edges between goal states
    path = []           # Final path to be returned
    visited = [start]   # All nodes that have been visited
    expansion = 0       # Number of expanded nodes

    goals.append(start)
    # This for loop determines the manhattan distance between any point and any other point
    # and stores the edge in an array
    for goal1 in goals:
        for goal2 in goals:
            if goal1 != goal2:
                dist = newstar.manhat(goal1, goal2)
                heapq.heappush(goal_edges, (dist, goal1, goal2))
                # path = newstar.astar(goal1, goal2)
                # heapq.heappush(goal_edges, (len(path), path))
    next = start
    while True:
        sep_goals = separate(goals)
        # Solve for the mst of the complete graph, excluding previously visited nodes
        goal_mst = mst(goal_edges, sep_goals, visited)

        # Determine the next node to be traversed
        next, expand1 = solve_costs(goal_mst, goals, next, visited, goal_edges)
        # Determine best path from last visited node to next
        temp_path, expand2 = newstar.astar(visited[-1], next)
        expansion += expand1 + expand2
        # temp_path = find_edge(visited[-1], next, goal_edges)[1]
        # del temp_path[-1]

        # If a node has been in the path and was not the end state, append to visited
        for node in temp_path:
            if node not in visited and node in goals:
                visited.append(node)

        path.extend(temp_path)
        for goal in goals:
            goal.neighbors = []

        # If all goal states have been visited, return path
        if len(visited) == len(goals):
            coords = [(node.y, node.x) for node in visited]
            print('Mult Expand: ', expansion, ' Mult path cost: ', len(path) - len(goals))
            return path, coords

# This solves for the next node to be traversed by applying the heuristic
# The heurisitc is the node with the minimum estimated path cost.  The path
# cost is determined as the walk with the largest weight that the node can form given the graph
# Params:
#   mst - Array of edges that form the MST
#   goals - Array of nodes that are the goal states
#   cur_node - Node that has currently been chosen to be traversed
#   visited - Array of all previously visited goal states
#   edges - Array of all edges in the complete graph
#
# Returns:
#   The next node to be traversed.  Also returns number of nodes expanded
def solve_costs(mst, goals, cur_node, visited, edges):
    min_node = None
    min_cost = 0
    expansion = 0
    for node1 in goals:
        if node1 not in visited:
            # base cost is the weight of the edge from the current node to the potential next node
            base_cost = find_edge(cur_node, node1, edges)[0]
            cost = base_cost
            for node2 in goals:
                if node1 != node2 and node2 not in visited:
                    # Find the cost of the walk from one node to the next by dfs
                    temp_cost, expand = modified_dfs(node1, node2, mst)
                    # Only take the largest individual cost given
                    if cost < temp_cost + base_cost:
                        cost = temp_cost + base_cost
                    expansion += expand
                    # Prune
                    if min_cost != 0 and cost > min_cost:
                        break
            # If cost is min, take this node as min
            if min_cost == 0 or cost < min_cost:
                min_cost = cost
                min_node = node1
    return min_node, expansion

# Helper function to find the edge associated with the 2 given nodes
# Params:
#   node1 - First node in edge
#   node2 - Second node in edge
#   edges - Array of edges
#
# Returns:
#   Edge tuple with weight and 2 nodes
def find_edge(node1, node2, edges):
    # cur_edge = [edge for edge in edges if 
    #                 (edge[1][0] == node1 and edge[1][-1] == node2) or
    #                 (edge[1][0] == node2 and edge[1][-1] == node1)]
    cur_edge = [edge for edge in edges if (edge[1] == node1 and edge[2] == node2) or
                    (edge[1] == node2 and edge[2] == node1)]
    return cur_edge[0]

# Helper function to create an array of arrays for Kruskal's Algo
# Params:
#   goals - Array of goal stats to be converted into array of arrays
#
# Returns:
#   Array of arrays of object in goals
def separate(goals):
    result = []
    for goal in goals:
        result.append([goal])
    return result

# Searches given array for the index of the array that contains node
# Params:
#   node - Node to look for
#   goals - Array of arrays that will be searched
#
# Returns:
#   index of array that contains node
def findset(node, goals):
    for i in range(len(goals)):
        if node in goals[i]:
            return i

# Combines lists in list of lists
# Params:
#   idx1 - Index of first list
#   idx2 - Index of second list
#   goals - List of lists that contain the set of nodes
def union(idx1, idx2, goals):
    for node in goals[idx2]:
        goals[idx1].append(node)
    goals.remove(goals[idx2])

# Creates an MST using Kruskal's Algo
# Params:
#   edges - List of edges in graph
#   goals - List of lists containing set of nodes
#   visited - All previously visited nodes
#
# Returns:
#   List of edges representing the MST
def mst(edges, goals, visited):
    mst_edges = []
    for edge in edges:
        # start_node = edge[1][0]
        # end_node = edge[1][-1]
        start_node = edge[1]
        end_node = edge[2]
        if start_node not in visited and end_node not in visited:
            start_idx = findset(start_node, goals)
            end_idx = findset(end_node, goals)
            if start_idx != end_idx:
                (start_node.neighbors).append(end_node)
                (end_node.neighbors).append(start_node)
                union(start_idx, end_idx, goals)
                mst_edges.append(edge)
    return mst_edges

# DFS function modified to work with edge tuple
# Params:
#   start - Beginning node
#   goal - End node
#   edges - All edges in graph
#
# Returns:
#   Weight of path from start to goal and number of nodes expanded
def modified_dfs(start, goal, edges):
    stack = LifoQueue()
    stack.put((start, [start], 0))
    expansion = 0

    while not stack.empty():
        node, path, weight = stack.get()
        expansion += 1
        if node == goal:
            return weight, expansion

        for neighbor in node.neighbors:
            if neighbor not in path:
                new_weight = find_edge(neighbor, node, edges)[0]
                stack.put((neighbor, path + [neighbor], weight + new_weight))

