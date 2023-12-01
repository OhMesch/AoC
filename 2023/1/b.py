numbers = [str(x) for x in range(1, 10)]
number_lookup = {'one': "1",
                 'two': "2",
                 'three': "3",
                 'four': "4",
                 'five': "5",
                 'six': "6",
                 'seven': "7",
                 'eight': "8",
                 'nine': "9"}
valid_digit_regex = f"({'|'.join(number_lookup.keys())}|\\d)"

def generateSolution(filename):
    running_sum = 0
    with open(filename) as f:
        for line in f:
            first = ""
            second = ""
            for i in range(len(line)):
                beginning_substring = line[0:i]
                possible = [n for n in numbers+list(number_lookup.keys()) if n in beginning_substring]
                if possible:
                    first = possible[0]
                    break
            for i in range(len(line)-1, -1, -1):
                ending_substring = line[i:]
                possible = [n for n in numbers+list(number_lookup.keys()) if n in ending_substring]
                if possible:
                    second = possible[0]
                    break
            combination_string = number_lookup.get(first, first) + number_lookup.get(second, second)
            running_sum += int(combination_string)
     
    return running_sum

if __name__ == "__main__":
    print(generateSolution("ab.dat"))