def generateSolution(filename):
    l = []
    r = []
    with open(filename) as f:
        for line in f:
            le,re = line.split()
            l.append(le)
            r.append(re)

    sum = 0
    for le in l:
        sum += int(le)*r.count(le)

    return sum

if __name__ == "__main__":
    print(generateSolution("ab.dat"))