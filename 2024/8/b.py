import re

def generateSolution(filename):
    with open(filename) as f:
        diskmap = f.read().strip()

    print()
    print(diskmap)
    occurrences = {}
    count = 0
    n_string = []
    for i, val in enumerate(diskmap):
        if i%2 == 0:
            occurrences[count] = int(val)
            n_string.extend([count]*int(val))
            count += 1
        else:
            n_string.extend([None]*int(val))

    # print(n_string)
    to_move = count-1
    while to_move:
        print(f"NEXT {to_move}")
        free_i = n_string.index(None)
        next_i = n_string.index(to_move)
        while free_i < next_i:
            free_size = 0
            while n_string[free_i] is not None:
                free_i += 1
            while free_i+free_size < next_i and n_string[free_i+free_size] is None:
                free_size += 1

            if occurrences[to_move] <= free_size:
                # print(f"Moving {to_move} with size {occurrences[to_move]}")
                move_idx = n_string.index(to_move)
                for _ in range(occurrences[to_move]):
                    n_string[free_i+_] = to_move
                    n_string[move_idx+_] = None
                # print(n_string)
                break
            else:
                free_i += free_size

        to_move -= 1
        # print()
    # print(n_string)


    # def pop_highest_fit(size):
    #     for i in range(len(num_occurrences)-1,-1,-1):
    #         if num_occurrences[i][1] <= size:
    #             return num_occurrences.pop(i)
    #     return None
    
    # n_string = []
    # zeros = num_occurrences.pop(0)
    # for _ in range(zeros[1]):
    #     n_string.append(0)

    # curr_pos = len(n_string)
    # while curr_pos < total_values:
    #     print("".join(str(x) if x is not None else "." for x in n_string))
    #     if len(free_size):
    #         next_free = free_size[0]

    #         for i,v in enumerate(num_occurrences):

    #         print(f"Next free size: {next_free_size}")
    #         while move_num:= pop_highest_fit(next_free_size):
    #             print(f"Number {move_num[0]} fits with size {move_num[1]}")
    #             for _ in range(move_num[1]):
    #                 n_string.append(move_num[0])
    #                 curr_pos += 1
    #                 next_free_size -= 1
    #         print(f"Excess free size: {next_free_size}")
    #         for _ in range(next_free_size):
    #             n_string.append(None)
    #             curr_pos += 1
    #     if len(num_occurrences):
    #         next_num = num_occurrences.pop(0)
    #         for _ in range(next_num[1]):
    #             n_string.append(next_num[0])
    #             curr_pos += 1
    #     else:
    #         break

    # print(n_string)
    # print("".join(str(x) if x is not None else "." for x in n_string))
    sol = 0
    for i,num in enumerate(n_string):
        if num:
            sol += i * num
    return sol

if __name__ == "__main__":
    print(generateSolution("ab.dat"))