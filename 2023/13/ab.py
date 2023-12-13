import numpy as np

def parseInputFile(filename):
    with open(filename, "r") as f:
        lines = [l.strip() for l in f.readlines()]
    
    mirror_matrix = []
    curr_mirror = []
    for line in lines:
        if line:
            curr_mirror.append(line)
        else:
            mirror_matrix.append(curr_mirror)
            curr_mirror = []
    mirror_matrix.append(curr_mirror)

    return mirror_matrix

def detectHorizontalMirror(mirror, required_smudges=1):
    for i in range(0, len(mirror)-1):
        segment_len = min(i+1, len(mirror)-i-1)
        low_idx = i-segment_len+1
        high_idx = i+segment_len

        smudges = 0
        while low_idx < high_idx and smudges <= required_smudges:
            smudges += sum([1 if mirror[low_idx][j] != mirror[high_idx][j] else 0 for j in range(0, len(mirror[low_idx]))])
            
            low_idx += 1
            high_idx -= 1

        if low_idx > high_idx and smudges == required_smudges:
            return i+1

    return None

def detectVerticalMirror(mirror, required_smudges):
    np_mirror = np.array([[c for c in l] for l in mirror], dtype=str)
    return detectHorizontalMirror(list(["".join(l) for l in np_mirror.T]), required_smudges)

def calculateMirrorValue(mirror, required_smudges):
    if h_idx := detectHorizontalMirror(mirror, required_smudges):
        return 100*h_idx
    elif v_idx := detectVerticalMirror(mirror, required_smudges):
        return v_idx

def generateSolution(filename, required_smudges=0):
    mirror_matrix = parseInputFile(filename)
    return sum([calculateMirrorValue(mirror, required_smudges) for mirror in mirror_matrix])
    
if __name__ == "__main__":
    print(generateSolution("ab.dat"))