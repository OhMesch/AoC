def generateSolution(filename, grid_size):
    with open(filename) as f:
        lines = [line.strip() for line in f.readlines()]

    grid = [['.' for _ in range(grid_size)] for _ in range(grid_size)]
    bytes = []
    for i in range(len(lines)):
        line = lines[i]
        x, y = [int(xy) for xy in line.split(",")]
        bytes.append((x, y))

    def print_grid():
        print()
        for row in grid:
            print("".join(row))
        print()

    def bfs(start, end):
        seen = set()
        queue = [start+([start],)]
        while queue:
            x, y, path = queue.pop(0)
            if 0 > x or x >= grid_size or 0 > y or y >= grid_size or grid[y][x] == "#" or (x, y) in seen:
                continue
            if (x, y) == end:
                return path
            
            seen.add((x, y))
            queue.append((x+1, y, path+[(x+1, y)]))
            queue.append((x-1, y, path+[(x-1, y)]))
            queue.append((x, y+1, path+[(x, y+1)]))
            queue.append((x, y-1, path+[(x, y-1)]))
        return []

    for i in range(grid_size):
        x, y = bytes.pop(0)
        if 0 <= x < grid_size and 0 <= y < grid_size:
            grid[y][x] = "#"
    
    curr_path = bfs((0, 0), (grid_size-1, grid_size-1))
    while len(curr_path) and len(bytes) > 0:
        print("Remaining Bytes:", len(bytes))
        x, y = bytes.pop(0)
        if 0 <= x < grid_size and 0 <= y < grid_size:
            grid[y][x] = "#"
        while (x, y) not in curr_path:
            x, y = bytes.pop(0)
            if 0 <= x < grid_size and 0 <= y < grid_size:
                grid[y][x] = "#"
        curr_path = bfs((0, 0), (grid_size-1, grid_size-1))
    
    print("No path")
    print(f"Bytes: {x},{y}")
    return f"{x},{y}"

if __name__ == "__main__":
    print(generateSolution("ab.dat", 71))