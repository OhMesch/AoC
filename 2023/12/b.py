from a import bruteForce

def generateSolution(filename):
    running_sum = 0

    with open(filename, "r") as f:
        lines = [l.strip() for l in f.readlines()]

    for i,line in enumerate(lines):
        parts, rules = line.split(" ")

        fifth_arrangement = 0
        first_arrangement = bruteForce(line)

        if first_arrangement:
            duplicate_line = "%s %s" % ('?'.join([parts for _ in range(2)]), (rules+',')*(1)+rules)
            second_arrangement = bruteForce(duplicate_line)
            fifth_arrangement = first_arrangement*(second_arrangement/first_arrangement)**4 if second_arrangement else 0

        # arrangements = bruteForce(new_line)
        print("%d/%d: %s -> %d | %d | %d" % (i, len(lines), line, first_arrangement, second_arrangement, fifth_arrangement))
        # # print(i + " " + len(lines)+": " + new_line)
        running_sum+=fifth_arrangement

    return running_sum
    
if __name__ == "__main__":
    print(generateSolution("ab.dat"))