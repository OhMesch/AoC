import re
import functools

FAILURE = 9999999999999999999999999999999
@functools.cache
def cheapestPath(ax, ay, bx, by, px, py):
    if px == 0 and py == 0:
        return 0
    if ax <= px and ay <= py and bx <= px and by <= py:
        return min(3+cheapestPath(ax, ay, bx, by, px-ax, py-ay), 1+cheapestPath(ax, ay, bx, by, px-bx, py-by))
    elif ax <= px and ay <= py:
        return 3+cheapestPath(ax, ay, bx, by, px-ax, py-ay)
    elif bx <= px and by <= py:
        return 1+cheapestPath(ax, ay, bx, by, px-bx, py-by)
    else:
        return FAILURE

def generateSolution(filename):
    with open(filename) as f:
        f_input = f.read().strip()

    all_A = re.findall(r"A:.*", f_input)
    all_B = re.findall(r"B:.*", f_input)
    all_prize = re.findall(r"Prize:.*", f_input)

    total_cost = 0
    for i in range(len(all_A)):
        ax, ay = map(int, re.findall(r"\d+", all_A[i]))
        bx, by = map(int, re.findall(r"\d+", all_B[i]))
        px, py = map(int, re.findall(r"\d+", all_prize[i]))

        # print(ax, ay, bx, by, px, py)
        cost = cheapestPath(ax, ay, bx, by, px, py)
        # print(cost)
        if cost < FAILURE:
            total_cost += cost

    return total_cost


if __name__ == "__main__":
    print(generateSolution("ab.dat"))