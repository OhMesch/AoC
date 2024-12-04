def generateSolution(filename):
    l = []
    r = []
    with open(filename) as f:
        for line in f:
            le,re = line.split()
            l.append(le)
            r.append(re)
            
    
    l = sorted([int(x) for x in l])
    r = sorted([int(x) for x in r])

    sum = 0
    for i in range(len(l)):
        sum += abs(l[i] - r[i])

    return sum

if __name__ == "__main__":
    print(generateSolution("ab.dat"))