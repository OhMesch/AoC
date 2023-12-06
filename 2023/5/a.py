import re

def organize_map(map_name, data):
    globals()[map_name] = []
    for line in data:
        dest_start, source_start, length = [int(v) for v in line.split()]
        globals()[map_name].append((dest_start, source_start, length))
    globals()[map_name].sort(key=lambda x: x[1])

def map_lookup(map, value):
    # I mean I should binary but...
    for dest_start, source_start, length in map:
        if source_start <= value < source_start + length:
            return dest_start + value - source_start
    return value

def generateSolution(filename):
    with open(filename) as f:
        data = f.read().strip()
    
    seed_line = re.search("seeds: (.*)", data, re.IGNORECASE).group(1)
    seeds = [int(seed.strip()) for seed in seed_line.split(" ")]

    while (match := re.search(r"(\w+)-to-(\w+) map:([\d\s]*)", data)):
        map_name = f"{match.group(1)}2{match.group(2)}"
        organize_map(map_name, [line.strip() for line in match.group(3).split("\n") if line.strip() != ""])
        
        data = re.sub(match.group(0), "", data)

    lowest_seen = float("inf")
    for s in seeds:
        soil = map_lookup(seed2soil, s)
        fertilizer = map_lookup(soil2fertilizer, soil)
        water = map_lookup(fertilizer2water, fertilizer)
        light = map_lookup(water2light, water)
        temperature = map_lookup(light2temperature, light)
        humidity = map_lookup(temperature2humidity, temperature)
        location = map_lookup(humidity2location, humidity)

        lowest_seen = min(lowest_seen, location)
    
    return lowest_seen

if __name__ == "__main__":
    print(generateSolution("ab.dat"))