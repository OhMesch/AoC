import re

def generateSolution(filename):
    with open(filename) as f:
        lines = f.readlines()
    
    maxH = len(lines)
    maxW = len(lines[0].strip())
    charString = [c for line in lines for c in line.strip()]

    vertStr = [charString[i*maxW:(i+1)*maxW] for i in range(maxW)]
    hortStr = [charString[i::maxW] for i in range(maxH)]
    diagXStr = [charString[i::maxW+1][:maxW-i] for i in range(maxW)]
    antiXStr = [charString[i::maxW-1][:i+1] for i in range(maxW)]
    diagYStr = [charString[i*maxW::maxW+1] for i in range(1,maxH)]
    antiYStr = [charString[i*maxW+maxW-1::maxW-1][:maxH-1] for i in range(1,maxH)]

    forwardStrings = vertStr + hortStr + diagXStr + diagYStr + antiXStr + antiYStr
    reverseStrings = [list(reversed(s)) for s in forwardStrings]
    allStrings = ["".join(sArr) for sArr in forwardStrings + reverseStrings if len(sArr) > 3]

    return sum([len(re.findall(r"XMAS", s)) for s in allStrings])

if __name__ == "__main__":
    print(generateSolution("ab.dat"))

# import functools

# @functools.cache
# def getNeighbors(x, y, grid_width, grid_height):
#     offsets = [
#         (-1, -1), (-1, 0), (-1, 1),
#         (0, -1),          (0, 1),
#         (1, -1), (1, 0), (1, 1)
#     ]
    
#     # Generate valid neighbors
#     neighbors = []
#     for dx, dy in offsets:
#         nx, ny = x + dx, y + dy
#         if 0 <= nx < grid_width and 0 <= ny < grid_height:
#             neighbors.append((nx, ny))
    
#     return neighbors


# next_letter = {"X": "M", "M": "A", "A": "S"}
# @functools.cache
# def isXmasDay(x, y, grid, requiredLetter, delta=None):
#     if grid[y][x] != requiredLetter:
#         return False
#     elif requiredLetter == "S":
#         return True

#     if delta:
#         return 0 <= x+delta[0] < len(grid[0]) and 0 <= y+delta[1] < len(grid) and isXmasDay(x + delta[0], y + delta[1], grid, next_letter[requiredLetter], delta)
#     else:
#         neighbors = getNeighbors(x, y, len(grid), len(grid[0]))
#         return any([isXmasDay(nx, ny, grid, next_letter[requiredLetter], (nx, ny)) for nx, ny in neighbors])

# def generateSolution(filename):
#     with open(filename) as f:
#         lines = f.readlines()
    
#     grid = tuple([tuple([c for c in line.strip()]) for line in lines])
#     return sum([isXmasDay(x, y, grid, "X") for y in range(len(grid)) for x in range(len(grid[0]))])
    
# if __name__ == "__main__":
#     print(generateSolution("ab.dat"))