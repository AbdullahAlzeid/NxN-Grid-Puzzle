from copy import deepcopy
import random
from collections import deque


def get_puzzle_size():
    while True:
        try:
            n = int(input('Enter the N value for puzzle size (3<=N<=6): '))
            if 3 <= n <= 6:
                return n
            else:
                print('Please Enter a Correct N Value!')
        except ValueError:
            print('Enter a valid integer!')


def solvable(state):
    n = len(state)
    flat_state = [tile for row in state for tile in row]
    inv_count = 0
    for i in range(n*n):
        for j in range(i+1, n*n):
            if flat_state[j] != 0 and flat_state[i] != 0 and flat_state[i] > flat_state[j]:
                inv_count += 1

    if n % 2 == 0:
        blank_row = [i for i, row in enumerate(state) if 0 in row][0]
        if blank_row % 2 == 0:
            return inv_count % 2 == 1
    return inv_count % 2 == 0


def generate_initial_state(n):
    while True:
        elements = list(range(1, n * n)) + [0]
        random.shuffle(elements)
        state = [elements[i * n:(i + 1) * n] for i in range(n)]
        if solvable(state):
            return state


def generate_goal_state(n):
    elements = list(range(1, n * n)) + [0]
    return [elements[i * n:(i + 1) * n] for i in range(n)]


def GenerateChildren(state, last_move=None):
    for i in range(len(state)):
        for j in range(len(state)):
            if state[i][j] == 0:
                oldi, oldj = (i, j)

    directions = [(-1, 0, "U"), (1, 0, "D"), (0, -1, "L"), (0, 1, "R")]
    successors = []

    opposite_moves = {"U": "D", "D": "U", "L": "R", "R": "L"}
    if last_move and last_move in opposite_moves:
        directions = [d for d in directions if d[2]
                      != opposite_moves[last_move]]

    for d in directions:
        newi, newj = oldi + d[0], oldj + d[1]

        if 0 <= newi < len(state) and 0 <= newj < len(state):
            child = deepcopy(state)
            child[oldi][oldj], child[newi][newj] = child[newi][newj], child[oldi][oldj]
            successors.append((child, d[2]))

    return successors


def Bfs(initial_state, goal_state):
    visited = set()
    queue = deque([(initial_state, [])])
    max_states = 0

    while queue:
        max_states = max(max_states, len(queue))
        current_state, path = queue.popleft()

        if current_state == goal_state:
            return path, max_states

        current_state_str = str(current_state)
        if current_state_str not in visited:
            visited.add(current_state_str)

            last_move = path[-1] if path else None
            for neighbor, move in GenerateChildren(current_state, last_move):
                queue.append((neighbor, path + [move]))

    return [], max_states

# This the Original DFS algorithm (Testing was done on the Iterative Deepening version as this version can get stuck in infinite loops and is heavily dependent on the initial configuration of the puzzle)
# def Original_Dfs(initial_state, goal_state):
#     stack = [(initial_state, [])]
#     max_states = 0

#     while stack:
#         max_states = max(max_states, len(stack))
#         current_state, path = stack.pop()

#         if current_state == goal_state:
#             return path, max_states

#         last_move = path[-1] if path else None
#         for neighbor, move in GenerateChildren(current_state, last_move):
#             stack.append((neighbor, path + [move]))

#     return [], max_states


# This is the Iterative Deepening version of DFS
def DFS(initial_state, goal_state):
    depth = 0
    while True:
        max_states = 0
        stack = [(initial_state, [], 0)]
        solution = None

        while stack:
            current_state, path, current_depth = stack.pop()

            if current_state == goal_state:
                return path, max_states

            max_states = max(max_states, len(stack))

            if current_depth < depth:
                last_move = path[-1] if path else None
                for neighbor, move in GenerateChildren(current_state, last_move):
                    stack.append((neighbor, path + [move], current_depth + 1))

        depth += 1


def Dfs_with_revisit_check(initial_state, goal_state):
    visited = set()
    stack = [(initial_state, [])]
    max_states = 0

    while stack:
        max_states = max(max_states, len(stack))
        current_state, path = stack.pop()

        if current_state == goal_state:
            del visited
            del stack
            return path, max_states

        current_state_str = str(current_state)
        if current_state_str not in visited:
            visited.add(current_state_str)

            last_move = path[-1] if path else None
            for neighbor, move in GenerateChildren(current_state, last_move):
                stack.append((neighbor, path + [move]))

    del visited
    del stack
    return [], max_states


def generate_report(algorithm_name, algorithm, n):

    splitter = "-" * 40 + "\n"

    with open("algorithm_report_DFS(Revisit check)4.txt", "w") as f:
        solution_depths = []
        states_stored = []

        for i in range(10):
            initial = generate_initial_state(n)
            final = generate_goal_state(n)

            solution_sequence, max_states_stored = algorithm(initial, final)
            solution_depth = len(solution_sequence)

            f.write(f"Run {i + 1}:\n")
            f.write("Initial State:\n")
            for row in initial:
                f.write(" ".join(map(str, row)) + "\n")
            f.write("\nFinal State:\n")
            for row in final:
                f.write(" ".join(map(str, row)) + "\n")
            f.write(f"\nAlgorithm Used: {algorithm_name}\n")
            f.write("Solution Sequence:\n")
            f.write(" --> ".join(solution_sequence) + "\n")
            f.write(f"\nSolution Depth: {solution_depth}\n")
            f.write(f"Max States Stored: {max_states_stored}\n\n")

            solution_depths.append(solution_depth)
            states_stored.append(max_states_stored)

            f.write(splitter)

        f.write("Descriptive Statistics:\n")
        f.write(f"Minimum Solution Depth: {min(solution_depths)}\n")
        f.write(f"Maximum Solution Depth: {max(solution_depths)}\n")
        f.write(
            f"Average Solution Depth: {sum(solution_depths) / len(solution_depths):.2f}\n")
        f.write(f"Minimum States Stored: {min(states_stored)}\n")
        f.write(f"Maximum States Stored: {max(states_stored)}\n")
        f.write(
            f"Average States Stored: {sum(states_stored) / len(states_stored):.2f}\n")


def main():

    n = get_puzzle_size()

    # # generate report used to get summary of the algorithm of choice

    # generate_report("DFS (With Revisit Check)", Dfs_with_revisit_check, n)

    Initial_State = generate_initial_state(n)

    Goal_State = generate_goal_state(n)

    print("\nInitial State:")
    for row in Initial_State:
        print(row)
    print("\nGoal State:")
    for row in Goal_State:
        print(row)

    print("\nFinding a Path Solution . . .\n")

    # Uncomment the method you want to use and store it in a variable

    # method = Bfs
    method = DFS
    # method = Dfs_with_revisit_check

    path, max_states = method(Initial_State, Goal_State)

    if path:
        print(f"Solution found through {method.__name__}!")
        print(" --> ".join(path))
        print(f"Solution depth: {len(path)}")
        print(f"Maximum number of states concurrently stored: {max_states}")
    else:
        print(f"No solution found using {method.__name__}.")


if __name__ == "__main__":
    main()
