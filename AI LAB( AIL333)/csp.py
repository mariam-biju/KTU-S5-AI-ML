def is_safe(graph, node, color, colors_given, names):
    for neighbor in graph[node]:
        if colors_given[neighbor] == color:
            return False
    return True

def graph_coloring(graph, colors, colors_given, node, names):
    if node == len(graph):
        return True    
    current_name = names[node]
    print(f"\nnode: {current_name}")
    available_colors = [color for color in colors if color not in [colors_given[neighbor] for neighbor in graph[node]]]
    print(f"available colors for {current_name}: {available_colors}")    
    for color in colors:
        if is_safe(graph, node, color, colors_given, names):
            colors_given[node] = color
            print(f"{current_name} is assigned {color}")
            if graph_coloring(graph, colors, colors_given, node + 1, names):
                return True
            print(f"backtracking from node {current_name}")
            colors_given[node] = None  
    return False

def main():
    n = int(input("enter the number of nodes: "))
    m = int(input("enter the number of edges: "))
    names = []
    for i in range(n):
        name = input(f"enter the name of node {i + 1}: ")
        names.append(name)
    graph = {i: [] for i in range(n)}    
    print("\nenter the edges pairwise by node names:")
    for _ in range(m):
        u_name, v_name = input().split()
        u = names.index(u_name)
        v = names.index(v_name)
        graph[u].append(v)
        graph[v].append(u)
    colors = input("\nenter the available colors (separated by spaces): ").split()
    colors_given = [None] * n    
    if graph_coloring(graph, colors, colors_given, 0, names):
        print("\nnode and corresponding colors: ")
        for i in range(n):
            print(f"node {names[i]} -> {colors_given[i]}")
    else:
        print("no solution")

main()
