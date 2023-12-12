import re
from functools import cache

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

@cache
def permutatePossible(parts, rules):
    parts, rules = simplify(parts, rules)
    if rules and '?' in parts:
        b1, b2 = parts.replace('?', '.', 1), parts.replace('?', '#', 1)
        return (permutatePossible(b1, rules) if isPossible(b1,rules) else 0) + (permutatePossible(b2, rules) if isPossible(b2,rules) else 0)
    else:
        return 1 if tuple([len(d) for d in re.findall(r'#+', parts)]) == rules else 0

total_p_list = []
def bruteForce(line):
    arrangements = 0
    parts,rules = line.split(" ")
    rules = [int(r) for r in rules.split(",")]

    arrangements += permutatePossible(parts, tuple(rules))
    # for p,r in part_list:
    #    arrangements += 1 if [len(d) for d in re.findall(r'#+', p)] == rules else 0
    # total_p_list.append(len(part_list))

    return arrangements

def generateSolution(filename):
    with open(filename, "r") as f:
        lines = [l.strip() for l in f.readlines()]

    ans = sum([bruteForce(line) for line in lines])
    print(permutatePossible.cache_info())
    return ans
    
if __name__ == "__main__":
    print(generateSolution("ab.dat"))