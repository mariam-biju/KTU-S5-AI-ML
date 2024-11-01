import heapq
GOAL_STATE = ((1, 2, 3), (4, 5, 6), (7, 8, 0))

def manhattan_distance(state):
    distance = 0
    for r in range(3):
        for c in range(3):
            value = state[r][c]
            if value != 0:
                goal_r, goal_c = divmod(value - 1, 3)
                distance += abs(r - goal_r) + abs(c - goal_c)
    return distance

def get_neighbors(state):
    def swap(state, r1, c1, r2, c2):
        state = [list(row) for row in state]
        state[r1][c1], state[r2][c2] = state[r2][c2], state[r1][c1]
        return tuple(tuple(row) for row in state)

    neighbors = []
    zero_r, zero_c = [(r, c) for r in range(3) for c in range(3) if state[r][c] == 0][0]
    moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up

    for move in moves:
        new_r, new_c = zero_r + move[0], zero_c + move[1]
        if 0 <= new_r < 3 and 0 <= new_c < 3:
            neighbors.append(swap(state, zero_r, zero_c, new_r, new_c))

    return neighbors

def best_first_search(start_state):
    open_list = [(manhattan_distance(start_state), start_state)]
    heapq.heapify(open_list)
    came_from = {start_state: None}
    cost_so_far = {start_state: 0}

    while open_list:
        _, current_state = heapq.heappop(open_list)
        
        if current_state == GOAL_STATE:
            path = []
            while current_state:
                path.append(current_state)
                current_state = came_from[current_state]
            path.reverse()
            return path

        for neighbor in get_neighbors(current_state):
            new_cost = cost_so_far[current_state] + 1  # Assuming each move has cost 1
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                priority = new_cost + manhattan_distance(neighbor)
                heapq.heappush(open_list, (priority, neighbor))
                came_from[neighbor] = current_state

    return []

def read_start_state():
    print("Enter the start state row by row, with space-separated numbers (use 0 for the empty space):")
    state = []
    for i in range(3):
        row = list(map(int, input(f"Row {i + 1}: ").strip().split()))
        if len(row) != 3:
            raise ValueError("Each row must have exactly 3 numbers.")
        state.append(tuple(row))
    return tuple(state)

def print_puzzle(state):
    for row in state:
        print(' '.join(map(str, row)))
    print()

start_state = read_start_state()
print("Start State:")
print_puzzle(start_state)

path = best_first_search(start_state)

if path:
    print("Solution Path:")
    for state in path:
        print_puzzle(state)
else:
    print("No solution found.")


