import re

def generateSolution(filename):
    games_list = []
    game_winnings = []
    for line in open(filename):
        card_halves = line.split(":")[1].strip().split("|")
        winning_numbers = [int(n) for n in re.findall(r"\d+", card_halves[0])]
        have_numbers = [int(n) for n in re.findall(r"\d+", card_halves[1])]
        
        games_list.append([winning_numbers, have_numbers])
        game_winnings.append(0)

    for i in range(len(games_list)-1,-1,-1):
        card_winning_numbers = games_list[i][0]
        card_have_numbers = games_list[i][1]
        card_have_winners = set(card_winning_numbers) & set(card_have_numbers)
        card_wins = len(card_have_winners)

        if card_wins == 0:
            game_winnings[i] = 1
        else:
            game_winnings[i] = 1+sum(game_winnings[i+1:i+card_wins+1])
    
    return sum(game_winnings)
    
if __name__ == "__main__":
    print(generateSolution("ab.dat"))