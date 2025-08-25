import os
import collections
import itertools
import time

grid = [
    ['#', 'S', '1', '1', '#'],
    [' ', '1', ' ', '#', '#'],
    ['#', '1', '1', '1', 'E'],
    ['#', '#', '', ' ', '#'],
]

def find_positions(grid, target):
    positions = []
    for r, row in enumerate(grid):
        for c, cell in enumerate(row):
            if cell == target:
                positions.append((r, c))
    return positions

def bfs(grid, start, goal):
    queue = collections.deque([[start]])
    visited = {start}
    while queue:
        path = queue.popleft()
        r, c = path[-1]
        if (r, c) == goal:
            return path
        for nr, nc in [(r, c+1), (r+1, c), (r, c-1), (r-1, c)]:
            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] != '#' and (nr, nc) not in visited:
                visited.add((nr, nc))
                queue.append(path + [(nr, nc)])
    return None

def find_best_path_collecting_ones(grid):
    start = find_positions(grid, 'S')[0]
    end = find_positions(grid, 'E')[0]
    ones = find_positions(grid, '1')
    shortest_full_path = None
    for perm in itertools.permutations(ones):
        full_path = []
        current = start
        success = True
        for target in list(perm) + [end]:
            segment = bfs(grid, current, target)
            if segment is None:
                success = False
                break
            if full_path:
                full_path += segment[1:]
            else:
                full_path += segment
            current = target
        if success and (shortest_full_path is None or len(full_path) < len(shortest_full_path)):
            shortest_full_path = full_path
    return shortest_full_path

def print_grid_with_s(grid, pos):
    
    for r, row in enumerate(grid):
        line = []
        for c, cell in enumerate(row):
            if (r, c) == pos:
                line.append('S')
            elif cell == 'S':
                line.append(' ')  # Remove old S position
            else:
                line.append(cell if cell else ' ')
        print(' '.join(line))
    print()

print("Finding path for S to collect all 1s and reach E...")
path = find_best_path_collecting_ones(grid)

if path:
    for step_num, position in enumerate(path):
        print_grid_with_s(grid, position)
        print(f"Step {step_num+1}/{len(path)}")
        time.sleep(2)  # Pause between moves
    print("Path complete!")
else:
    print("No path found.")
