from a import parseInputFile, hashWord

from collections import OrderedDict
import re

def generateSolution(filename):
    hash_map = [None for _ in range(256)]
    initialization_sequence = parseInputFile(filename)

    split_pattern = re.compile(r'-|=')
    for label, lense in [re.split(split_pattern, w) for w in initialization_sequence]:
        box_number = hashWord(label)
        if hash_map[box_number] is None:
            hash_map[box_number] = OrderedDict()
        if lense:
            hash_map[box_number][label] = int(lense)
        elif label in hash_map[box_number]:
            del hash_map[box_number][label]

    focus_power = 0
    for box_idx, box in enumerate(hash_map):
        if box: 
            focus_power += sum([(box_idx+1)*(lense_idx+1)*lense_power for lense_idx, lense_power in enumerate(box.values())])

    return focus_power
    
if __name__ == "__main__":
    print(generateSolution("ab.dat"))