import numpy as np

def parseInputFile(filename):
    hailstorm_trajectories = []
    with open(filename, "r") as f:
        for line in f:
            position, velocity = line.split("@")
            position = [int(xyz) for xyz in position.strip().split(', ')]
            velocity = [int(xyz) for xyz in velocity.strip().split(', ')]
            hailstorm_trajectories.append([position, velocity])
    return hailstorm_trajectories

def convertToEquations(hailstorm_trajectories):
    equation_matrix = []
    for hailstorm in hailstorm_trajectories:
        hailstorm_slope = hailstorm[1][1] / hailstorm[1][0]
        hailstorm_intercept = hailstorm[0][1] - hailstorm_slope * hailstorm[0][0]
        equation_matrix.append(([-hailstorm_slope, 1], [hailstorm_intercept]))
    return equation_matrix

def solveEquations(equation1, equation2):
    try:
        return np.linalg.solve(np.vstack((equation1[0], equation2[0])), np.vstack((equation1[1], equation2[1])))
    except:
        return None

def generateSolution(filename, limits):
    hailstorm_trajectories = parseInputFile(filename)
    hailstorm_equations = convertToEquations(hailstorm_trajectories)

    collisions_in_range = 0
    for i in range(len(hailstorm_equations)):
        for j in range(i + 1, len(hailstorm_equations)):
            solve = solveEquations(hailstorm_equations[i], hailstorm_equations[j])
            if np.all(solve != None):
                if np.all(limits[0] < solve[:,0]) and np.all(solve[:,0] < limits[1]):
                    #bet can put this in matrix for solving
                    h1_time = (solve[0,0]-hailstorm_trajectories[i][0][0])/hailstorm_trajectories[i][1][0]
                    h2_time = (solve[0,0]-hailstorm_trajectories[j][0][0])/hailstorm_trajectories[j][1][0]
                    if np.all(np.array([h1_time, h2_time]) >= 0):
                        print()
                        print(hailstorm_trajectories[i], hailstorm_trajectories[j])
                        print(f"Collision at {solve[0,0]}, {solve[1,0]}")
                        collisions_in_range += 1
    return collisions_in_range
    
    
    
if __name__ == "__main__":
    print(generateSolution("ab.dat", [200000000000000, 400000000000000]))