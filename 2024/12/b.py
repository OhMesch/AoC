def generateSolution(filename):
    with open(filename) as f:
        crops = [[c for c in line.strip()] for line in f.readlines()]

    seen = set()
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def exploreArea(crop_type, x, y):
        if x < 0 or y < 0 or x >= len(crops[0]) or y >= len(crops) or (x, y) in seen or crops[y][x] != crop_type:
            return
        seen.add((x, y))
        current_area.add((x, y))
        for dx, dy in directions:
            exploreArea(crop_type, x+dx, y+dy)

    def explorePerimeter(crop_type, area):
        perm = set()
        for x, y in area:
            for dx, dy in directions:
                if x+dx < 0 or y+dy < 0 or x+dx >= len(crops[0]) or y+dy >= len(crops) or crops[y+dy][x+dx] != crop_type:
                    perm.add((x+dx, y+dy, (dx, dy)))
        return perm

    price = 0
    for y in range(len(crops)):
        for x in range(len(crops[y])):
            if (x,y) not in seen:
                # print(f"\nNEW AREA {crops[y][x]}")
                current_area = set()
                exploreArea(crops[y][x], x, y)
                perm = explorePerimeter(crops[y][x], current_area)
                straight_lines = 0
                for px, py, (dx, dy) in perm:
                    if (px-1, py, (dx, dy)) not in perm and (px, py-1, (dx, dy)) not in perm:
                        straight_lines += 1
                # print(crops[y][x], len(current_area), len(current_fencing), len(current_area) * len(current_fencing))
                # print(crops[y][x], len(current_area), straight_lines, len(current_area) * straight_lines)
                # print(current_area, current_fencing)
                price += len(current_area) * straight_lines
                # if crops[y][x] == "I":
                #     exit()
    return price
    

if __name__ == "__main__":
    print(generateSolution("ab.dat"))