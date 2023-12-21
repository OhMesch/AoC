from a import parseInputFile
from functools import cache

@cache
def exploreAdjacent(origin, garden_grid):
    x, y = origin
    return [(x+dx,y+dy) for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)] if garden_grid[(y+dy)%len(garden_grid)][(x+dx)%len(garden_grid[0])] == '.']

def exploreGarden(start, garden_grid, steps):
    new_can_reach_by_step = [{start}, exploreAdjacent(start, garden_grid)]

    for step in range(2, steps+1):
        new_can_reach = set()
        for prior_pos in new_can_reach_by_step[step-1]:
            [new_can_reach.add(adj) for adj in exploreAdjacent(prior_pos, garden_grid) if adj not in new_can_reach_by_step[step-2]]
        new_can_reach_by_step.append(new_can_reach)

    return new_can_reach_by_step

def printRed(tezt):
    print(f"\033[91m{tezt}\033[00m")
def look_repeating(seq):
    import collections
    import more_itertools

    for size in range(3, len(seq)//2):
        windows = [
            tuple(window)
            for window in more_itertools.windowed(seq, size)
        ]
        counter = collections.Counter(windows)
        for window, count in counter.items():
            if count > 1:
                printRed(window, count)

def generateSolution(filename, steps = 26501365):
    start, garden_grid = parseInputFile(filename)
    exploration = exploreGarden(start, garden_grid, steps)
    print(f"Even Expansion:")
    e_o = [len(exploration[i]) for i in range(0, steps+1, 2)]
    print("Pure")
    print(e_o)
    look_repeating(e_o)
    print("diff")
    print([e_o[i]-e_o[i-1] for i in range(1, len(e_o))])
    look_repeating([e_o[i]-e_o[i-1] for i in range(1, len(e_o))])
    print('ratio')
    print([round(e_o[i]/e_o[i-1],5) for i in range(1, len(e_o))])
    look_repeating([round(e_o[i]/e_o[i-1],5) for i in range(1, len(e_o))])
    print()
    print(f"Odd Expansion:")
    o_o = [len(exploration[i]) for i in range(1, steps+1, 2)]
    look_repeating(o_o)
    print("Pure")
    print(o_o)
    print('diff')
    print([o_o[i]-o_o[i-1] for i in range(1, len(o_o))])
    look_repeating([o_o[i]-o_o[i-1] for i in range(1, len(o_o))])
    print('ratio')
    print([round(o_o[i]/o_o[i-1], 5) for i in range(1, len(o_o))])
    look_repeating([round(o_o[i]/o_o[i-1], 5) for i in range(1, len(o_o))])

    print()
    print(f"Full")
    f_o = [len(exploration[i]) for i in range(0, steps+1)]
    look_repeating(f_o)
    print("diff")
    print([f_o[i]-f_o[i-1] for i in range(1, len(f_o))])
    look_repeating([f_o[i]-f_o[i-1] for i in range(1, len(f_o))])
    print('ratio')
    print([round(f_o[i]/f_o[i-1],5) for i in range(1, len(f_o))])
    look_repeating([round(f_o[i]/f_o[i-1],5) for i in range(1, len(f_o))])

    if steps % 2 == 0:
        return sum(e_o)
    else:
        return sum(o_o)
    return len(exploration[steps])
    
if __name__ == "__main__":
    print(generateSolution("ab.dat", 2000))