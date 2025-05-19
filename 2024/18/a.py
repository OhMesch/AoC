def generateSolution(filename, grid_size):
    with open(filename) as f:
        lines = [line.strip() for line in f.readlines()]

    simulation_max = 1024
    simulation_max = 12

    grid = [['.' for _ in range(grid_size)] for _ in range(grid_size)]
    for i in range(simulation_max):
        line = lines[i]
        x, y = [int(xy) for xy in line.split(",")]
        if 0 <= x < grid_size and 0 <= y < grid_size:
            grid[y][x] = "#"

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

    print_grid()
    return len(bfs((0, 0), (grid_size-1, grid_size-1)))-1

if __name__ == "__main__":
    print(generateSolution("ab.dat", 71))