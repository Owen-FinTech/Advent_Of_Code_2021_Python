import heapq
from collections import defaultdict
from copy import deepcopy

# Define hallway positions where amphipods can stop (columns)
HALLWAY_POSITIONS = [1, 2, 4, 6, 8, 10, 11]

# Mapping of amphipod type to their target room column
TARGET_ROOMS = {
    'A': 3,
    'B': 5,
    'C': 7,
    'D': 9,
}

# Energy cost per step for each amphipod type
ENERGY_COST = {
    'A': 1,
    'B': 10,
    'C': 100,
    'D': 1000,
}

# Depth of rooms (number of positions vertically in a room)
ROOM_DEPTH = 4  # Updated for Part 2

class Option:
    def __init__(self, grid: tuple, energy: int):
        self.grid = grid
        self.energy = energy

    def __lt__(self, other):
        return self.energy < other.energy

# Updated Initial Configuration with inserted lines
input_string = '''#############
#...........#
###D#A#D#C###
  #D#C#B#A#
  #D#B#A#C#
  #C#A#B#B#
  #########'''  # Insert your puzzle input between the triple quotes

# Updated Final Configuration with inserted lines
final_string = '''#############
#...........#
###A#B#C#D###
  #A#B#C#D#
  #A#B#C#D#
  #A#B#C#D#
  #########'''

input_split = [list(line) for line in input_string.strip().split("\n")]
final_split = [list(line) for line in final_string.strip().split("\n")]

def grid_to_tuple(grid):
    return tuple("".join(row) for row in grid)

initial_grid = grid_to_tuple(input_split)
final_grid = grid_to_tuple(final_split)

def get_possible_moves(grid):
    moves = []
    grid_list = [list(row) for row in grid]  # Convert to mutable list of lists

    # Identify positions of all amphipods
    for i, row in enumerate(grid_list):
        for j, cell in enumerate(row):
            if cell in ['A', 'B', 'C', 'D']:
                amphipod = cell
                target_col = TARGET_ROOMS[amphipod]

                # Determine if the amphipod is in the hallway
                if i == 1:
                    # Amphipod is in the hallway, try to move it to its target room
                    # Check if the target room is ready (only contains same type or is empty)
                    room_row = None
                    for depth in range(2, 2 + ROOM_DEPTH):
                        if grid_list[depth][target_col] == '.':
                            room_row = depth
                        elif grid_list[depth][target_col] != amphipod:
                            room_row = None
                            break
                    if room_row is not None:
                        # Check if the hallway path is clear
                        path_clear = True
                        start = min(j, target_col)
                        end = max(j, target_col)
                        for hallway_col in range(start, end + 1):
                            if hallway_col == j:
                                continue
                            if grid_list[1][hallway_col] != '.':
                                path_clear = False
                                break
                        if path_clear:
                            # Calculate steps: horizontal distance + vertical distance
                            steps = abs(j - target_col) + (room_row - 1)
                            energy = steps * ENERGY_COST[amphipod]

                            # Create new grid state
                            new_grid = deepcopy(grid_list)
                            new_grid[i][j] = '.'
                            new_grid[room_row][target_col] = amphipod
                            new_grid_tuple = grid_to_tuple(new_grid)
                            moves.append((new_grid_tuple, energy))
                    continue  # Move to next amphipod

                # Amphipod is in a room
                # Check if it's already in the correct room and no blocking amphipods
                if j == TARGET_ROOMS[amphipod]:
                    # Check if all amphipods below are correct
                    correct = True
                    for depth in range(i + 1, 2 + ROOM_DEPTH):
                        if grid_list[depth][j] != amphipod:
                            correct = False
                            break
                    if correct:
                        continue  # No need to move this amphipod

                # Amphipod needs to move out of the room
                # Check if there are amphipods blocking it
                blocking = False
                for depth in range(2, i):
                    if grid_list[depth][j] != '.':
                        blocking = True
                        break
                if blocking:
                    continue  # Cannot move this amphipod

                # Determine possible hallway positions to move to
                for hallway_col in HALLWAY_POSITIONS:
                    # Check if the path to the hallway position is clear
                    path_clear = True
                    start = min(j, hallway_col)
                    end = max(j, hallway_col)
                    for col in range(start, end + 1):
                        if grid_list[1][col] != '.':
                            if col == j:
                                continue
                            path_clear = False
                            break
                    if path_clear:
                        # Calculate steps: horizontal distance + vertical distance
                        steps = abs(j - hallway_col) + (i - 1)
                        energy = steps * ENERGY_COST[amphipod]

                        # Create new grid state
                        new_grid = deepcopy(grid_list)
                        new_grid[i][j] = '.'
                        new_grid[1][hallway_col] = amphipod
                        new_grid_tuple = grid_to_tuple(new_grid)
                        moves.append((new_grid_tuple, energy))

    return moves

def solve_amphipod(initial_grid, final_grid):
    initial_option = Option(initial_grid, 0)
    heap = []
    heapq.heappush(heap, initial_option)

    visited = {}

    while heap:
        current_option = heapq.heappop(heap)

        # Check if the current state is the final state
        if current_option.grid == final_grid:
            print(f"Minimum energy required: {current_option.energy}")
            return current_option.energy

        # Skip if this state has been visited with a lower energy
        if current_option.grid in visited and visited[current_option.grid] <= current_option.energy:
            continue

        # Mark this state as visited
        visited[current_option.grid] = current_option.energy

        # Generate all possible moves from the current state
        for new_grid, move_energy in get_possible_moves(current_option.grid):
            total_energy = current_option.energy + move_energy

            # If the new state hasn't been visited or has a lower energy, add it to the heap
            if new_grid not in visited or total_energy < visited[new_grid]:
                new_option = Option(new_grid, total_energy)
                heapq.heappush(heap, new_option)

    # If the final state was never reached
    print("No solution found.")
    return None

if __name__ == "__main__":
    solve_amphipod(initial_grid, final_grid)
