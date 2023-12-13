import re
from functools import cache
import a

def simplify(parts, rules):
    parts = re.sub(r"^\.*", "", parts)
    parts = re.sub(r"\.*$", "", parts)
    parts = re.sub(r"\.+", ".", parts)

    while rules and (simple_parts := re.sub(r"^#{" + str(rules[0]) + r"\.*", "", parts)) != parts:
        parts = simple_parts
        rules = tuple(rules[1:])

    while rules and (simple_parts := re.sub(r"\.+#{" + str(rules[-1]) + r"}$", "", parts)) != parts:
        parts = simple_parts
        rules = tuple(rules[:-1])

    while rules and ((simple_parts := re.sub(r"^#[^.]{" + str(rules[0]-1) + r"}[^#]", ".", parts)) != parts):
        # print("\n",parts, rules, simple_parts, tuple(rules[1:]))
        parts = simple_parts
        rules = tuple(rules[1:])

    while rules and ((simple_parts := re.sub(r"[^#][^.]{" + str(rules[-1]-1) + r"}#$", ".", parts)) != parts):
        # print("\n",parts, rules, simple_parts, tuple(rules[:-1]))
        parts = simple_parts
        rules = tuple(rules[:-1])

    return parts, rules

def isPossible(parts, rules):
    # Exists any damage group larger than any rule or any damage group too large for corresponding rule
    damage_groups_len = [len(d) for d in re.findall(r'#+', parts)]
    if len(damage_groups_len) and max(damage_groups_len) > max(rules):
        return False

    # Exists all possible damage group smaller than any rule or any possible damage group too small for corresponding rule
    possible_damage_group_len = [len(g) for g in re.findall(r"[^.]+", parts)]
    if len(possible_damage_group_len) and max(possible_damage_group_len) < max(rules):
        return False
    
    # Too many possible damage groups exist
    if len([g for g in re.findall(r"[^.]+", parts) if '#' in g]) > len(rules):
        return False

    # Too many damaged exist in group
    alone_damage_groups_len = [len(d)-1 for d in re.findall(r'#+[.]', parts)]
    if len(alone_damage_groups_len) > len(rules):
        return False
    # Single damaged group too large for placement
    if len(alone_damage_groups_len) == len(rules):
        for g,r in zip(alone_damage_groups_len, rules):
            if g > r:
                return False

    return True

@cache
def permutatePossible(parts, rules, d=0):
    parts, rules = simplify(parts, rules)
    # if d==0:
    #     print()
    # print(f"String: '{parts}' w/ Rules {rules} - Depth: {d}")
    if rules and '?' in parts:
        size = rules[0]

        all_possibles=[]
        first_cluster = re.search(r'#+', parts)
        possible_range = min(first_cluster.end(), len(parts)-size) if first_cluster else len(parts)-size
        for i in range(possible_range+1):
            if "." not in parts[i:i+size] and (i == 0 or parts[i-1] != "#") and (i+size >= len(parts) or parts[i+size] != "#"):
                fill = '#'*size + '.'*(1 if (i+size < len(parts) and parts[i+size] == '?') else 0)
                # print("\033[95m" + parts[:i].replace("?",".")+f"\033[95m{fill}\033[0m" + parts[i+len(fill):])
                all_possibles.append(parts[:i].replace("?",".")+parts[i+len(fill):])
        
        # print("Recalling:")
        # [print(p, tuple(rules[1:])) for p in all_possibles if (not rules[1:] or isPossible(p, tuple(rules[1:])))]
        # sums = [permutatePossible(p, tuple(rules[1:]),d=d+1) for p in all_possibles if (not rules[1:] or isPossible(p, tuple(rules[1:])))]
        return sum([permutatePossible(p, tuple(rules[1:]),d=d+1) for p in all_possibles if (not rules[1:] or isPossible(p, tuple(rules[1:])))])
    else:
        # print("COMPLETE: ", parts, rules, "=>", 1 if tuple([len(d) for d in re.findall(r'#+', parts)]) == rules else 0, "\n")
        return 1 if tuple([len(d) for d in re.findall(r'#+', parts)]) == rules else 0

total_p_list = []
def bruteForce(line):
    arrangements = 0
    parts,rules = line.split(" ")
    rules = [int(r) for r in rules.split(",")]

    arrangements += permutatePossible(parts, tuple(rules))

    return arrangements

def generateSolution(filename):
    running_sum = 0
    with open(filename, "r") as f:
        lines = [l.strip() for l in f.readlines()]

    for i,line in enumerate(lines):
        parts, rules = line.split(" ")

        duplicate_line = "%s %s" % ('?'.join([parts for _ in range(5)]), (rules+',')*(4)+rules)

        arrangement = bruteForce(duplicate_line)
        print("%d/%d: %s -> %d" % (i, len(lines), line, arrangement))
        running_sum+=arrangement


    # ans = sum([bruteForce(line) for line in lines])
    print(permutatePossible.cache_info())
    return running_sum
    
if __name__ == "__main__":
    print(generateSolution("ab.dat"))