from a import find_difference

def predict_sequence(sequence):
    diffs = [sequence]
    while any(diffs[-1]):
        diffs.append(find_difference(diffs[-1]))

    for i in range(len(diffs)-2,-1,-1):
        diffs[i].insert(0, diffs[i][0] - diffs[i+1][0])
    return diffs[0][0]

def generateSolution(filename):
    sequences = []
    sequence_predictions = []
    with open(filename) as f:
        for line in f.readlines():
            sequences.append([int(num) for num in line.split()])    

    for s in sequences:
        sequence_predictions.append(predict_sequence(s))

    return sum(sequence_predictions)
    
if __name__ == "__main__":
    print(generateSolution("ab.dat"))