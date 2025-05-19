def generateSolution(filename):
    with open(filename) as f:
        crops = [[c for c in line.strip()] for line in f.readlines()]

    seen = set()
    explore_directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    # fence_directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1)]

    def explore(crop_type, x, y):
        if x < 0 or y < 0 or x >= len(crops[0]) or y >= len(crops) or (x, y) in seen or crops[y][x] != crop_type:
            return
        seen.add((x, y))
        current_area.add((x, y))
        for dx, dy in explore_directions:
            if x+dx < 0 or y+dy < 0 or x+dx >= len(crops[0]) or y+dy >= len(crops) or crops[y+dy][x+dx] != crop_type:
                current_fencing.append((x+dx, y+dy))
        for dx, dy in explore_directions:
            explore(crop_type, x+dx, y+dy)
    
    price = 0
    for y in range(len(crops)):
        for x in range(len(crops[y])):
            if (x,y) not in seen:
                current_area = set()
                current_fencing = []
                explore(crops[y][x], x, y)
                # print(crops[y][x], len(current_area), len(current_fencing), len(current_area) * len(current_fencing))
                # print(current_area, current_fencing)
                price += len(current_area) * len(current_fencing)
                # if crops[y][x] == "I":
                #     exit()
    return price
    

if __name__ == "__main__":
    print(generateSolution("ab.dat"))