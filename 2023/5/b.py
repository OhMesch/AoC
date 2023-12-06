import re

def organize_map(map_name, data):
    globals()[map_name] = []
    for line in data:
        dest_start, source_start, length = [int(v) for v in line.split()]
        globals()[map_name].append((dest_start, source_start, length))
    globals()[map_name].sort(key=lambda x: x[1])

def combine_maps(input_map, output_map):
    combined_map = []
    unaccounted_for = set(input_map+output_map)
    print(f"{input_map=}")
    print(f"{output_map=}")
    
    for out_set in output_map:
        out_dest, out_src, out_len = out_set
        for in_set in input_map:
            in_dest, in_src, in_len = in_set
            min_start = min(in_dest, out_src)
            max_start = max(in_dest, out_src)
            min_end = min(in_dest+in_len, out_src+out_len)
            max_end = max(in_dest+in_len, out_src+out_len)
            if max_start < min_end:
                overlap_len = min_end-max_start
                overlap = ((out_dest, out_src + in_src - in_dest, overlap_len))
                print(f"{overlap=}")

                left_in = ((in_dest, in_src, out_src-in_dest))
                print(f"{left_in=}")
                left_out = ((out_dest, out_src, in_src-out_src))
                print(f"{left_out=}")


                right_in = ((in_dest+overlap_len, in_src+overlap_len, in_len-overlap_len))
                right_out = ((out_dest+overlap_len, out_src+overlap_len, out_len-overlap_len))
                print(f"{right_in=}")
                print(f"{right_out=}")

                for new_range in [left_in, left_out, overlap, right_in, right_out]:
                    if new_range[2] > 0:
                        combined_map.append(new_range)

                if in_set in unaccounted_for:
                    unaccounted_for.remove(in_set)
                if out_set in unaccounted_for:
                    unaccounted_for.remove(out_set)

    # Add any remaining unaccounted for ranges and return
    combined_map.extend(list(unaccounted_for))
    return combined_map

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

    temperature2location = combine_maps(temperature2humidity, humidity2location)
    light2location = combine_maps(light2temperature, temperature2location)
    water2location = combine_maps(water2light, light2location)
    fertilizer2location = combine_maps(fertilizer2water, water2location)
    soil2location = combine_maps(soil2fertilizer, fertilizer2location)
    seed2location = combine_maps(seed2soil, soil2location)

    lowest_seen = float("inf")
    for s_base, s_range in zip(seeds[::2], seeds[1::2]):
        for s_index in range(s_range):
            lowest_seen = min(lowest_seen, map_lookup(seed2location, s_base+s_index))

    return lowest_seen

if __name__ == "__main__":
    print(generateSolution("ab.dat"))