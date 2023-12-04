import re

def generateSolution(filename):
    running_sum = 0

    for line in open(filename):
        card_halves = line.split(":")[1].strip().split("|")
        winning_numbers = [int(n) for n in re.findall(r"\d+", card_halves[0])]
        have_numbers = [int(n) for n in re.findall(r"\d+", card_halves[1])]

        have_winners = set(winning_numbers) & set(have_numbers)
        points = 2**(len(have_winners)-1) if have_winners else 0
        running_sum += points
    
    return running_sum
    
if __name__ == "__main__":
    print(generateSolution("ab.dat"))