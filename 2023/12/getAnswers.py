if __name__ == "__main__":
    with open("b.dat", "r") as f:
        lines = [l.strip() for l in f.readlines()]

    counter = 0
    for line in lines:
        data = line.split("->")[1]
        (f,s,c) = [int(c.strip()) for c in data.split("|")]
        new_c = (s/f)**(4)*f
        if new_c != int(new_c):
            print(f"{counter}: {f} {s} => {new_c} | {c}")
        counter += 1