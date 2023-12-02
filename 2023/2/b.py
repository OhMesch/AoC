import re

def generateSolution(filename):
    running_sum = 0
    for line in open(filename):
        cube_pulls = line.replace(r"Game (\d+):\s*", "").strip().split("; ")

        rgb_matches = [[re.search(r"(\d+)\s*red", pull, re.IGNORECASE),
                       re.search(r"(\d+)\s*green", pull, re.IGNORECASE),
                       re.search(r"(\d+)\s*blue", pull, re.IGNORECASE)] for pull in cube_pulls]
        
        cube_max_counts = [(max([int(pull[0].group(1)) if pull[0] else 0 for pull in rgb_matches])),
                           (max([int(pull[1].group(1)) if pull[1] else 0 for pull in rgb_matches])),
                           (max([int(pull[2].group(1)) if pull[2] else 0 for pull in rgb_matches]))]
        
        running_sum += cube_max_counts[0] * cube_max_counts[1] * cube_max_counts[2]

    return running_sum
    
if __name__ == "__main__":
    print(generateSolution("ab.dat"))