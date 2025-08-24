import os
import collections

# The maze for the agent to solve
grid = [
    ['#', 'S', ' ', ' ', '#'],
    [' ', '1', ' ', '#', '#'],
    ['#', ' ', ' ', '1', 'E'],
    ['#', '#', ' ', ' ', '#'],
]

def find_start_position(grid):
    """
    Finds the starting 'S' in the grid using simple loops.
    Returns a tuple (row, col) or None if not found.
    """
    for r, row in enumerate(grid):
        for c, cell in enumerate(row):
            if cell == 'S':
                return (r, c)
    return None

def solve_with_bfs(grid):
    """
    Finds the shortest path from 'S' to 'E' using BFS.
    """
    start_pos = find_start_position(grid)
    if not start_pos:
        print("Error: Start 'S' not found.")
        return None

    # Set up the queue with the initial path (containing only the start position)
    queue = collections.deque([ [start_pos] ])
    visited = {start_pos}

    # Process the queue until a path to 'E' is found
    while queue:
        current_path = queue.popleft()
        r, c = current_path[-1] # Our current position

        # Check for the goal
        if grid[r][c] == 'E':
            return current_path # Success! Return the shortest path.

        # Explore neighbors (Right, Down, Left, Up)
        for next_r, next_c in [(r, c + 1), (r + 1, c), (r, c - 1), (r - 1, c)]:
            # Check if the neighbor is valid and has not been visited
            if (0 <= next_r < len(grid) and 0 <= next_c < len(grid[0])) and \
               grid[next_r][next_c] != '#' and (next_r, next_c) not in visited:
                
                visited.add((next_r, next_c))
                # Create the new path and add it to the queue to be explored
                new_path = current_path + [(next_r, next_c)]
                queue.append(new_path)
    
    # If the queue becomes empty, 'E' is unreachable
    return None

# --- Main Program Execution ---
print("Agent is finding the shortest path from 'S' to 'E' using BFS...")
solution_path = solve_with_bfs(grid)

if solution_path:
    print("Agent found the shortest path!")
    
    # After the path is found, calculate the score based on that path
    score = sum(1 for r, c in solution_path if grid[r][c] == '1')
    
    # Display the final grid with the path marked by '*'
    os.system('cls' if os.name == 'nt' else 'clear')
    display_grid = [row[:] for row in grid]
    for r, c in solution_path:
        if display_grid[r][c] not in ('S', 'E'):
            display_grid[r][c] = '*'
    
    for row in display_grid:
        print(' '.join(row))
        
    print(f"\nPath: {solution_path}")
    print(f"Path Length: {len(solution_path) - 1} steps")
    print(f"Final Score: {score}")
else:
    print("Agent could not find a path to 'E'.")
