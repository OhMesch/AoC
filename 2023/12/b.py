from a import bruteForce

def generateSolution(filename):
    running_sum = 0

    with open(filename, "r") as f:
        lines = [l.strip() for l in f.readlines()]

    for i,line in enumerate(lines):
        parts, rules = line.split(" ")

        duplicate_line = "%s %s" % ('?'.join([parts for _ in range(5)]), (rules+',')*(4)+rules)

        arrangement = bruteForce(duplicate_line)
        print("%d/%d: %s -> %d" % (i, len(lines), line, arrangement))
        running_sum+=arrangement

    return running_sum
    
if __name__ == "__main__":
    print(generateSolution("ab.dat"))