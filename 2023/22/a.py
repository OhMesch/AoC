import re

def parseInputFile(filename):
    with open(filename, "r") as f:
        return sorted([tuple(int(dim) for dim in t) for t in re.findall(r"(\d+),(\d+),(\d+)~(\d+),(\d+),(\d+)", f.read())], key=lambda x: (x[2], x[0], x[1]))

def printRed(tezt):
    print(f"\033[91m{tezt}\033[00m")

def printGreen(tezt):
    print(f"\033[92m{tezt}\033[00m")

def buildSandBlockColumn(sand_blocks):
    #ranges are pretty small on block size so can use range dict
    block_lookup = {}
    block_column = {}
    block_dependencies = {}
    for i,block_dims in enumerate(sand_blocks):
        # block_name = hex(i)
        block_name = ""
        while i > 0:
            block_name = chr(ord('a')+i%26)+block_name
            i = i//26
        block_name = block_name or "a"
        
        x1,y1,z1,x2,y2,z2 = block_dims
        print()
        print(block_name, ":",x1,y1,z1,"->",x2,y2,z2)
        
        lands_on = 0
        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                if x in block_lookup and y in block_lookup[x] and block_column[x][y] >= lands_on:
                    if block_column[x][y] > lands_on:
                        lands_on = block_column[x][y]
                        block_dependencies[block_name] = []
                        printGreen(f"New high point for {block_name} at {x},{y},{lands_on}. Clearing dependencies.")
                    depend_name = block_lookup[x][y][lands_on]
                    print(f"{block_name} lands on {depend_name} at {x},{y},{lands_on}")
                    if depend_name not in block_dependencies[block_name]:
                        block_dependencies[block_name].append(depend_name)
        print(f"{block_name} depends on {block_dependencies.get(block_name, [])}")
        if (z2-z1+lands_on+1 > z2 or lands_on+1 > z1):
            printRed(f"Block {block_name} falls up {x1},{y1},{z2}")
        z2 = z2-z1+lands_on+1 #sit on top of the block
        z1 = lands_on+1

        print(block_name,"falls to:",x1,y1,z1,"->",x2,y2,z2)
        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                block_column.setdefault(x, {})[y] = z2
                for z in range(z1, z2+1):
                    block_lookup.setdefault(x, {}).setdefault(y, {})[z] = block_name
    print()
    print(f"block_column: {block_column}")
    print(f"block_dependencies: {block_dependencies}")
    print(f"block_lookup: {block_lookup}")
    return block_column, block_dependencies

def generateSolution(filename):
    sand_blocks = parseInputFile(filename)
    sand_block_column, sand_block_dependencies = buildSandBlockColumn(sand_blocks)

    essential = set()
    for v in sand_block_dependencies.values():
        if len(v) == 1:
            essential.add(v[0])
    return len(sand_blocks)-len(essential)
    
    
    
if __name__ == "__main__":
    print(generateSolution("ab.dat"))