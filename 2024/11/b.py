import functools

def generateSolution(filename):
    with open(filename) as f:
        stones = [int(c) for c in f.read().strip().split()]

    @functools.cache
    def shiftStone(stone, n):
        shifted = []
        if stone == 0:
            shifted.append(1)
        elif len(str(stone))%2 == 0:
            h1, h2 = str(stone)[:len(str(stone))//2], str(stone)[len(str(stone))//2:]
            shifted.extend([int(h1), int(h2)])
        else:
            shifted.append(stone*2024)
        if n > 1:
            if len(shifted) > 1:
                return shiftStone(shifted[0], n-1) + shiftStone(shifted[1], n-1)
            else:
                return shiftStone(shifted[0], n-1)
        else:
            return len(shifted)

    stone_len = 0
    for stone in stones:
        stone_len += shiftStone(stone, 75)
    print(shiftStone.cache_info())

    return(stone_len)

if __name__ == "__main__":
    print(generateSolution("ab.dat"))