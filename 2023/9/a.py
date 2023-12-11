def find_difference(sequence):
    return [(sequence[i] - sequence[i-1]) for i in range(1, len(sequence))]

def predict_sequence(sequence):
    diffs = [sequence]
    while any(diffs[-1]):
        diffs.append(find_difference(diffs[-1]))

    for i in range(len(diffs)-2,-1,-1):
        diffs[i].append(diffs[i][-1] + diffs[i+1][-1])
    return diffs[0][-1]

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