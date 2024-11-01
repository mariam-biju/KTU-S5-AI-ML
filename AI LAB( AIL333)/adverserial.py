import math

class TreeNode:
    def __init__(self, name, value=None):
        self.name = name
        self.value = value
        self.children = []
    
    def add_child(self, child):
        self.children.append(child)

def print_tree(node, level=0):
    indent = "  " * level
    if not node.children: 
        print(f"{indent}Leaf {node.name}: {node.value}")
    else:
        print(f"{indent}Node {node.name}")
        for child in node.children:
            print_tree(child, level + 1)

def alpha_beta(node, depth, alpha, beta, max_turn, visited_nodes, path):
    if depth == 0 or not node.children:
        visited_nodes.add(node.name)
        return node.value, path

    if max_turn:
        value = float('-inf')
        best_path = None
        for child in node.children:
            visited_nodes.add(node.name)
            current_value, current_path = alpha_beta(child, depth - 1, alpha, beta, False, visited_nodes, path + [child.name])
            if current_value > value:
                value = current_value
                best_path = current_path
            alpha = max(alpha, value)
            if beta <= alpha:
                break
        return value, best_path
    else:
        value = float('inf')
        best_path = None
        for child in node.children:
            visited_nodes.add(node.name)
            current_value, current_path = alpha_beta(child, depth - 1, alpha, beta, True, visited_nodes, path + [child.name])
            if current_value < value:
                value = current_value
                best_path = current_path
            beta = min(beta, value)
            if beta <= alpha:
                break
        return value, best_path

def build_tree_from_input():
    d = int(input("Enter the depth of the tree: "))
    num_nodes = int(input("Enter the number of nodes: "))
    nodes = {}

    for _ in range(num_nodes):
        name = input("Enter the name for the node: ").upper()
        nodes[name] = TreeNode(name)
    
    for name in nodes:
        children_names = input(f"Enter the names of the children for node {name} (space-separated): ").upper().split()
        for child_name in children_names:
            if child_name in nodes:
                nodes[name].add_child(nodes[child_name])
            else:
                print(f"Warning: Child node {child_name} does not exist.")
    
    for name in nodes:
        if not nodes[name].children:  
            value = int(input(f"Enter value for leaf node {name}: "))
            nodes[name].value = value

    root_name = list(nodes.keys())[0]
    return nodes[root_name], d

def minimax(node, depth, is_maximizing, path):
    if depth == 0 or not node.children:
        return node.value if node.value is not None else 0, path

    if is_maximizing:
        best_value = -math.inf
        best_path = None
        for child in node.children:
            value, current_path = minimax(child, depth - 1, False, path + [child.name])
            if value > best_value:
                best_value = value
                best_path = current_path
        return best_value, best_path
    else:
        best_value = math.inf
        best_path = None
        for child in node.children:
            value, current_path = minimax(child, depth - 1, True, path + [child.name])
            if value < best_value:
                best_value = value
                best_path = current_path
        return best_value, best_path

def print_pruned_tree(node, visited_nodes, level=0):
    indent = "  " * level
    if node.name in visited_nodes:
        if not node.children:  # Leaf node
            print(f"{indent}Leaf {node.name}: {node.value}")
        else:
            print(f"{indent}Node {node.name}")
            for child in node.children:
                print_pruned_tree(child, visited_nodes, level + 1)
    else:
        # Print pruned nodes in a different format
        print(f"{indent}Pruned Node {node.name} (Not Visited)")

def main_menu():
    print("BUILD THE TREE : ")
    root, depth = build_tree_from_input()
    
    while True:
        print("\nMenu:")
        print("1. Minimax")
        print("2. Alpha-Beta Pruning")
        print("3. Exit")
        
        choice = input("Enter your choice: ").strip()
        
        if choice == '1':
            print("Tree structure:")
            print_tree(root)
            is_maximizing = True
            
            depth = int(input("Enter the depth for the Minimax algorithm: "))
            best_value, best_path = minimax(root, depth, is_maximizing, [root.name])
            print("\nThe best value for the maximizing player is:", best_value)
            print("The best path taken is:", " -> ".join(best_path))
        
        elif choice == '2':
            print("Tree structure:")
            print_tree(root)
            
            visited_nodes = set()
            optimal_value, best_path = alpha_beta(root, depth, float('-inf'), float('inf'), True, visited_nodes, [root.name])
            
            print("\nTree structure after pruning:")
            print_pruned_tree(root, visited_nodes)
            print("\nThe optimal value is:", optimal_value)
            print("The best path taken is:", " -> ".join(best_path))
        
        elif choice == '3':
            print("Exiting program.")
            break
        
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main_menu()


