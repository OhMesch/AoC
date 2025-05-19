def generateSolution(filename):
    with open(filename) as f:
        diskmap = f.read().strip()

    print()
    print(diskmap)
    n_string = []
    count = 0
    for i, val in enumerate(diskmap):
        if i%2 == 0:
            for _ in range(int(val)):
                n_string.append(count)
            count += 1
        else:
            for j in range(int(val)):
                n_string.append(-1)

    sol = 0
    i = 0
    while i < len(n_string):
        curr_val = n_string[i]
        if curr_val >= 0:
            sol += curr_val*i
            print(f"{curr_val} * {i} = {curr_val*i}")
        else:
            top_val = n_string.pop()
            while len(n_string) and top_val < 0:
                top_val = n_string.pop()
            if top_val > 0:
                sol += top_val*i
                print(f"{top_val} * {i} = {top_val*i}")
        i+=1
    return sol

if __name__ == "__main__":
    print(generateSolution("ab.dat"))