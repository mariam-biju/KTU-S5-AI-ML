from collections import deque

def bfs(tree, start, goal):
    visited = set()
    queue = deque([start])
    result = []
   
    while queue:
        vertex = queue.popleft()
        if vertex == goal:
            result.append(vertex)
            break
        if vertex not in visited:
            visited.add(vertex)
            result.append(vertex)
            queue.extend(neighbour for neighbour in tree[vertex] if neighbour not in visited)

    return result

def dfs(tree, start, goal, visited=None):
    if visited is None:
        visited = set()
   
    visited.add(start)
    result = [start]
   
    if start == goal:
        return result

    for neighbour in tree[start]:
        if neighbour not in visited:
            path = dfs(tree, neighbour, goal, visited)
            result.extend(path)
            if goal in path:
                return result

    return result
	
def read():
    tree = {}
    num_nodes = int(input("Enter the number of nodes: "))
    num_branch = int(input("Enter the number of branches: "))
   
    for _ in range(num_branch):
        u, v = input("Enter an branches : ").split()
        if u not in tree:
            tree[u] = []
        if v not in tree:
            tree[v] = []
        tree[u].append(v)
        tree[v].append(u)
   
    return tree

tree = read()
start_node = input("Enter the starting node: ")
goal_node = input("Enter the goal node: ")
bfs_result = bfs(tree, start_node, goal_node)
dfs_result = dfs(tree, start_node, goal_node)
print("BFS Traversal:", bfs_result)
print("DFS Traversal:", dfs_result)


