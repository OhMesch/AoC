from a import parseInputFile, buildSandBlockColumn

from functools import cache

def chainReact(dependencies):
    supports = {}
    for dependant, depends_on in dependencies.items():
        for depend_on_block in depends_on:
            supports.setdefault(depend_on_block, set()).add(dependant)

    @cache
    def removeSupportAndGetFalls(removed):
        print("removeSupportAndGetFalls", removed)
        nonlocal dependencies, supports
        next_to_fall = set()
        for r_block in removed:
            for upstream_block in supports.get(r_block, []):
                if upstream_block not in removed and len(dependencies[upstream_block]-set(removed)) == 0:
                    next_to_fall.add(upstream_block)        
        if len(next_to_fall) == 0:
            return 0
        return len(next_to_fall) + removeSupportAndGetFalls(tuple(sorted(list(next_to_fall|set(removed)))))
    
    holds_up = {k: removeSupportAndGetFalls((k,)) for k in supports.keys()}

    print(removeSupportAndGetFalls.cache_info())
    # print()
    # print("dpendencies")
    # print({k: dependencies[k] for k in sorted(dependencies.keys())})
    # print()
    # print("supports")
    # print({k: supports[k] for k in sorted(supports.keys())})
    # print()
    # print("holds_up")
    # print({k: holds_up[k] for k in sorted(holds_up.keys())})

    return sum(holds_up.values())

def generateSolution(filename):
    sand_blocks = parseInputFile(filename)
    _, sand_block_dependencies = buildSandBlockColumn(sand_blocks)
    sand_block_dependencies = {k: set(v) for k, v in sand_block_dependencies.items()}
    return chainReact(sand_block_dependencies)
    
if __name__ == "__main__":
    print(generateSolution("ab.dat"))