def parseInputFile(filename):
    with open(filename, "r") as f:
        return f.readline().strip().split(',')

def hashWord(word):
    hash = 0
    for c in word:
        hash += ord(c)
        hash *= 17
        hash %= 256
    return hash

def generateSolution(filename):
    initialization_sequence = parseInputFile(filename)
    return sum([hashWord(w) for w in initialization_sequence])
    
if __name__ == "__main__":
    print(generateSolution("ab.dat"))