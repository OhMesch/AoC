import re
import math

def count_solutions(time, record):
    # should just do half the range, binary search it to find when we start to win, then x2 and account for odd, but yet...
    distances = [t*(time-t) for t in range(1,time+1)]
    return len([d for d in distances if d > record])

def generateSolution(filename):
    with open(filename) as f:
        lines = [l.strip() for l in f.readlines()]
    
    times = [int(t) for t in re.findall(r"\d+", lines[0])]
    distances = [int(d) for d in re.findall(r"\d+", lines[1])]

    solutions = []
    for t,d in zip(times, distances):
        solutions.append(count_solutions(t,d))

    return math.prod(solutions)
    
if __name__ == "__main__":
    print(generateSolution("ab.dat"))