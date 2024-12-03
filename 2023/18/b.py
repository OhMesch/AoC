import numpy as np

def parseInputFile(filename):
    dig_instructions = []
    with open(filename, "r") as f:
        for _, _, hex_string in [l.split() for l in f.readlines()]:
            distance, direction = hex_string[2:-2], hex_string[-2:-1]
            dig_instructions.append((direction, int(distance, 16)))
    return dig_instructions

direction_map = {
    "0": np.array([1, 0]),
    "1": np.array([0, -1]),
    "2": np.array([-1, 0]),
    "3": np.array([0, 1]),
}
def generateDigVertices(dig_instructions):
    vertices = []
    curr_point = np.array([0, 0])
    
    for direction, distance in dig_instructions:
        vertices.append(curr_point)
        curr_point = curr_point + direction_map[direction] * distance

    return vertices

#Shoelace formula
def calculatePolygonArea(vertices):
    a = 0
    b = 0
    for i in range(len(vertices)):
        curr_v = vertices[i]
        next_v = vertices[(i+1)%len(vertices)]
        a += curr_v[0]*next_v[1]
        b += curr_v[1]*next_v[0]
        print()
        print(curr_v, next_v)
        print(a,b)
    print(1/2*abs(b-a))

    return 1/2*abs(sum([np.cross(vertices[i], vertices[(i+1)%len(vertices)]) for i in range(len(vertices))]))

def calculatePolygonPerimeter(vertices):
    return sum([np.linalg.norm(vertices[i] - vertices[(i+1)%len(vertices)]) for i in range(len(vertices))])

def generateSolution(filename):
    dig_instructions = parseInputFile(filename)
    vertices = generateDigVertices(dig_instructions)

    #picks theorem
    picks_theorem_interior_points = calculatePolygonArea(vertices) - calculatePolygonPerimeter(vertices)/2 + 1

    return picks_theorem_interior_points + calculatePolygonPerimeter(vertices)
    
    
if __name__ == "__main__":
    print(generateSolution("ab.dat"))