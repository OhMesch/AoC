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
                printRed((window, count))

def generateSolution(filename, steps = 26501365):
    start, garden_grid = parseInputFile(filename)

    garden_size = len(garden_grid)
    pattern_runs = garden_size*10
    if pattern_runs > steps:
        exploration = exploreGarden(start, garden_grid, steps)
        new_pos_at_step = [len(e) for e in exploration]
    else:
        exploration = exploreGarden(start, garden_grid, pattern_runs)
        new_pos_at_step = [len(e) for e in exploration]
        
        exploration_modulo = [[] for _ in range(garden_size)]
        for i, e in enumerate(new_pos_at_step):
            if i != 0: exploration_modulo [i%garden_size].append(e)
        exploration_modulo  = [tuple(group) for group in exploration_modulo]

        diff_within_module = []
        for t in exploration_modulo:
            curr = []
            for i in range(1, len(t)):
                curr.append(t[i]-t[i-1])
            diff_within_module.append(curr)

        for i in range(pattern_runs+1, steps+1):
            new_pos_at_step.append(new_pos_at_step[i-garden_size]+diff_within_module[i%garden_size][-1])

    return sum([new_pos_at_step[i] for i in range(steps % 2, steps+1, 2)])
    
if __name__ == "__main__":
    print(generateSolution("ab.dat", 26501365))