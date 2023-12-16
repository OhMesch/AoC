from a import seen_paths, energized, laser_explore, parseInputFile
import numpy as np

import sys
sys.setrecursionlimit(10000)

def generateSolution(filename):
    contraption_grid = parseInputFile(filename)

    max_energized = 0
    rot_table = {"\\": "/", "/": "\\", "-": "|", "|": "-"}
    rot_translation_table = str.maketrans(rot_table)
    for _ in range(4):
        contraption_grid = np.rot90(contraption_grid, k=-1)
        contraption_grid = np.array([[s.translate(rot_translation_table) for s in row] for row in contraption_grid])

        for start_idx in range(len(contraption_grid)):
            energized.clear()
            seen_paths.clear()
            
            laser_start, laser_initial_move = np.array([-1,start_idx]), np.array([0, start_idx])
            laser_explore(contraption_grid, laser_start, laser_initial_move)
            max_energized = max(max_energized, len(energized))

    return max_energized
    
if __name__ == "__main__":
    print(generateSolution("ab.dat"))