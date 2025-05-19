def generateSolution(filename):
    with open(filename) as f:
        stones = [int(c) for c in f.read().strip().split()]

    def shiftStones(stones):
        shifted = []
        for stone in stones:
            if stone == 0:
                shifted.append(1)
            elif len(str(stone))%2 == 0:
                h1, h2 = str(stone)[:len(str(stone))//2], str(stone)[len(str(stone))//2:]
                shifted.extend([int(h1), int(h2)])
            else:
                shifted.append(stone*2024)
        return shifted

    for i in range(25):
        # print(stones)
        stones = shiftStones(stones)

    return(len(stones))

if __name__ == "__main__":
    print(generateSolution("ab.dat"))