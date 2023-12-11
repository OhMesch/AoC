import numpy as np

def generateSolution(filename, expansion=1000000):
    with open(filename, "r") as f:
        space_grid = np.array([list(l.strip()) for l in f.readlines()], dtype=str)

    expanded_rows = [i for i,r in enumerate(space_grid) if "#" not in r]
    expanded_cols = [i for i,c in enumerate(np.transpose(space_grid)) if "#" not in c]
    
    galaxies_i = np.where(space_grid == "#")
    galaxies = [xy for xy in zip(galaxies_i[1], galaxies_i[0])]

    running_sum = 0
    for i,(x_1, y_1) in enumerate(galaxies):
        for j,(x_2, y_2) in enumerate(galaxies[i+1:]):
            # print(f"({i+1}->{i+2+j}): {abs(x_1-x_2) + abs(y_1-y_2) + (expansion-1)*len([c for c in expanded_cols if c in range(min(x_1,x_2)+1, max(x_1,x_2))]) + (expansion-1)*len([r for r in expanded_rows if r in range(min(y_1,y_2)+1, max(y_1,y_2))])}")
            running_sum += abs(x_1-x_2) + abs(y_1-y_2) + (expansion-1)*len([c for c in expanded_cols if c in range(min(x_1,x_2)+1, max(x_1,x_2))]) + (expansion-1)*len([r for r in expanded_rows if r in range(min(y_1,y_2)+1, max(y_1,y_2))])

    return running_sum
    
if __name__ == "__main__":
    print(generateSolution("ab.dat", 2))
    print(generateSolution("ab.dat", 1000000))