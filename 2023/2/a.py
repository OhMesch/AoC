import re

red_limit = 12
green_limit = 13
blue_limit = 14

def generateSolution(filename):
    running_sum = 0
    for line in open(filename):
        id_match = re.search(r"Game (\d+):\s*", line, re.IGNORECASE)
        line = line.replace(id_match.group(0), "").strip()

        cube_pulls = line.split("; ")
        rgb_matches = [[re.search(r"(\d+)\s*red", pull, re.IGNORECASE),
                       re.search(r"(\d+)\s*green", pull, re.IGNORECASE),
                       re.search(r"(\d+)\s*blue", pull, re.IGNORECASE)] for pull in cube_pulls]

        counts = []
        for match in rgb_matches:
            counts.append([int(m.group(1)) if m else 0 for m in match])

        if all([True if (c[0] <= red_limit and c[1] <= green_limit and c[2] <= blue_limit) else False for c in counts]):
            running_sum += int(id_match.group(1))

    return running_sum
    
if __name__ == "__main__":
    print(generateSolution("ab.dat"))