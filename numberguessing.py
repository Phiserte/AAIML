def print_grid(rows, cols, char='-'):
    """Creates and prints a grid of specified dimensions."""
    grid = [[char for _ in range(cols)] for _ in range(rows)]
    for row in grid:
        print(' '.join(row))

# --- Run Program ---
print("--- 4x5 Grid ---")
print_grid(4, 5)

print("\n--- 3x3 Grid with '*' ---")
print_grid(3, 3, char='*')```

### 2. ASCII Grid Finder Program

```python
def find_character_locations(grid_lines, target_char):
    """Finds all occurrences of a target character in a grid."""
    locations = []
    for r, row in enumerate(grid_lines):
        for c, char in enumerate(row):
            if char == target_char:
                locations.append((r, c))
    return locations

# --- Run Program ---
ascii_grid = """
+----------+
|S..T......|
|...T......|
|.......T.|
+----------+
"""

grid_as_list = ascii_grid.strip().split('\n')

start_positions = find_character_locations(grid_as_list, 'S')
task_positions = find_character_locations(grid_as_list, 'T')

print(f"Start 'S' found at: {start_positions[0] if start_positions else 'None'}")
print(f"Tasks 'T' found at: {task_positions}")
