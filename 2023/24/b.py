from a import parseInputFile

import random

import numpy as np

def generateSolution(filename):
    hailstorm_trajectories = parseInputFile(filename)
    random_hailstorms = [hailstorm_trajectories[i] for i in random.sample(range(len(hailstorm_trajectories)), 8)]
    hail_coeff = []
    hail_sol = []
    for i in range(0,len(random_hailstorms), 2):
        eq1_coeff = np.array([random_hailstorms[i][1][1], -random_hailstorms[i][1][0], -random_hailstorms[i][0][1], random_hailstorms[i][0][0]])
        eq2_coeff = np.array([random_hailstorms[i+1][1][1], -random_hailstorms[i+1][1][0], -random_hailstorms[i+1][0][1], random_hailstorms[i+1][0][0]])
        hail_coeff.append(eq1_coeff-eq2_coeff)

        eq1_sol = np.array([(random_hailstorms[i][1][1]*random_hailstorms[i][0][0])-(random_hailstorms[i][1][0]*random_hailstorms[i][0][1])])
        eq2_sol = np.array([(random_hailstorms[i+1][1][1]*random_hailstorms[i+1][0][0])-(random_hailstorms[i+1][1][0]*random_hailstorms[i+1][0][1])])
        hail_sol.append(eq1_sol-eq2_sol)
    x,y,vx,vy = np.linalg.solve(np.vstack(hail_coeff), np.vstack(hail_sol))

    random_hailstorms = [hailstorm_trajectories[i] for i in random.sample(range(len(hailstorm_trajectories)), 8)]
    hail_coeff = []
    hail_sol = []
    for i in range(0,len(random_hailstorms), 2):
        eq1_coeff = np.array([random_hailstorms[i][1][2], -random_hailstorms[i][1][1], -random_hailstorms[i][0][2], random_hailstorms[i][0][1]])
        eq2_coeff = np.array([random_hailstorms[i+1][1][2], -random_hailstorms[i+1][1][1], -random_hailstorms[i+1][0][2], random_hailstorms[i+1][0][1]])
        hail_coeff.append(eq1_coeff-eq2_coeff)

        eq1_sol = np.array([(random_hailstorms[i][1][2]*random_hailstorms[i][0][1])-(random_hailstorms[i][1][1]*random_hailstorms[i][0][2])])
        eq2_sol = np.array([(random_hailstorms[i+1][1][2]*random_hailstorms[i+1][0][1])-(random_hailstorms[i+1][1][1]*random_hailstorms[i+1][0][2])])
        hail_sol.append(eq1_sol-eq2_sol)
    y,z,vy,vz = np.linalg.solve(np.vstack(hail_coeff), np.vstack(hail_sol))
    print(x,y,z)
    np.set_printoptions(formatter={'float_kind':'{:f}'.format})
    print(sum([x,y,z]))
    return(sum([x,y,z]))
    
    
if __name__ == "__main__":
    print(generateSolution("ab.dat"))