def is_valid_move(grid, x, y):
    return 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] != 'X'

def count_possible_paths(grid, start, max_steps):
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    visited = set()
    queue = deque([(start, 0)])  # Each queue element: ((x, y), steps)
    possible_paths = 0

    while queue:
        (x, y), steps = queue.popleft()
        if grid[x][y] == 'C':
            possible_paths += 1
        if steps >= max_steps:
            continue

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if is_valid_move(grid, nx, ny) and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append(((nx, ny), steps + 1))

    return possible_paths

grid = [
    ['0', '0', '0', '0', '0', '0', 'X', 'C' ],
    ['0', '0', '0', '0', 'C', '0', 'X', 'X' ],
    ['0', '0', 'S', '0', '0', '0', '0', '0' ],
    ['0', '0', '0', '0', '0', '0', '0', '0' ],
    ['0', '0', '0', '0', '0', '0', 'C', 'X' ]
]

robot_location = (2, 2)
max_steps = 5

possible_paths = count_possible_paths(grid, robot_location, max_steps)
print("Number of possible paths:", possible_paths)
