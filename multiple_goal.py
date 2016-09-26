import newstar, heapq, copy, IPython
from queue import LifoQueue

def mult(start, goals):
    goal_edges = []
    path = []
    visited = [start]
    expansion = 0

    goals.append(start)
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
        goal_mst = mst(goal_edges, sep_goals, visited)

        next, expand1 = solve_costs(goal_mst, goals, next, visited, goal_edges)
        temp_path, expand2 = newstar.astar(visited[-1], next)
        expansion += expand1 + expand2
            # temp_path = find_edge(visited[-1], next, goal_edges)[1]
            # del temp_path[-1] 

        for node in temp_path:
            if node not in visited and node in goals:
                visited.append(node)

        path.extend(temp_path)
        for goal in goals:
            goal.neighbors = []

            # visited.append(next)

        if len(visited) == len(goals):
            coords = [(node.y, node.x) for node in visited]
            print('Mult Expand: ', expansion, ' Mult path cost: ', len(path) - len(goals))
            return path, coords

def solve_costs(mst, goals, cur_node, visited, edges):
    min_node = None
    min_cost = 0
    expansion = 0
    for node1 in goals:
        if node1 not in visited:
            base_cost = find_edge(cur_node, node1, edges)[0]
            cost = base_cost
            for node2 in goals:
                if node1 != node2 and node2 not in visited:
                    temp_cost, expand = modified_dfs(node1, node2, mst)
                    if cost < temp_cost + base_cost:
                        cost = temp_cost + base_cost
                    expansion += expand
                    if min_cost != 0 and cost > min_cost:
                        break

            if min_cost == 0 or cost < min_cost:
                min_cost = cost
                min_node = node1
    return min_node, expansion

def find_edge(node1, node2, edges):
    # cur_edge = [edge for edge in edges if 
    #                 (edge[1][0] == node1 and edge[1][-1] == node2) or
    #                 (edge[1][0] == node2 and edge[1][-1] == node1)]
    cur_edge = [edge for edge in edges if (edge[1] == node1 and edge[2] == node2) or
                    (edge[1] == node2 and edge[2] == node1)]
    return cur_edge[0]


def separate(goals):
    result = []
    for goal in goals:
        result.append([goal])
    return result

def findset(node, goals):
    for i in range(len(goals)):
        if node in goals[i]:
            return i

def union(node1, node2, goals):
    for node in goals[node2]:
        goals[node1].append(node)
    goals.remove(goals[node2])

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

