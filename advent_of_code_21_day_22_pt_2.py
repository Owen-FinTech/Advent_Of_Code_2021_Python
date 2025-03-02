input_string = '''''' # Insert your puzzle input between the triple quotes

splitString = input_string.split("\n")
cuboid = []

for line in splitString:
    cuboidLine = []
    splitLine = line.split(" ")

    if splitLine[0] == "on":
        cuboidLine.append(1)
    else:
        cuboidLine.append(0)

    currNums = ""
    for i in range(0, len(splitLine[1])):
        if splitLine[1][i].isnumeric() or splitLine[1][i] == "-":
            currNums += splitLine[1][i]
        else:
            if len(currNums) > 0:
                cuboidLine.append(int(currNums))
            currNums = ""

    cuboidLine.append(int(currNums))
    cuboid.append(cuboidLine)


class Cube:
    def __init__(self, onOff: int, x1: int, x2: int, y1: int, y2: int, z1: int, z2: int):
        self.onOff = onOff
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.z1 = z1
        self.z2 = z2

    def switch(self, onOff: int):
        self.onOff = onOff 

def vol(cube: Cube) -> int:
    # Calculate the volume of the cube
    return max(0, (cube.x2 - cube.x1 + 1)) * max(0, (cube.y2 - cube.y1 + 1)) * max(0, (cube.z2 - cube.z1 + 1))

def subtract(cube1: Cube, cube2: Cube) -> list:
    # Subtract cube2 from cube1 and return the resulting non-overlapping cubes
    result = []

    if not (cube2.x1 <= cube1.x2 and cube2.x2 >= cube1.x1 and
            cube2.y1 <= cube1.y2 and cube2.y2 >= cube1.y1 and
            cube2.z1 <= cube1.z2 and cube2.z2 >= cube1.z1):
        return [cube1]

    # Determine the bounds of the overlap
    oLap_x1 = max(cube1.x1, cube2.x1)
    oLap_x2 = min(cube1.x2, cube2.x2)
    oLap_y1 = max(cube1.y1, cube2.y1)
    oLap_y2 = min(cube1.y2, cube2.y2)
    oLap_z1 = max(cube1.z1, cube2.z1)
    oLap_z2 = min(cube1.z2, cube2.z2)

    # Create the non-overlapping cubes
    if cube1.x1 < oLap_x1:
        result.append(Cube(1, cube1.x1, oLap_x1 - 1, cube1.y1, cube1.y2, cube1.z1, cube1.z2))
    if oLap_x2 < cube1.x2:
        result.append(Cube(1, oLap_x2 + 1, cube1.x2, cube1.y1, cube1.y2, cube1.z1, cube1.z2))
    if cube1.y1 < oLap_y1:
        result.append(Cube(1, oLap_x1, oLap_x2, cube1.y1, oLap_y1 - 1, cube1.z1, cube1.z2))
    if oLap_y2 < cube1.y2:
        result.append(Cube(1, oLap_x1, oLap_x2, oLap_y2 + 1, cube1.y2, cube1.z1, cube1.z2))
    if cube1.z1 < oLap_z1:
        result.append(Cube(1, oLap_x1, oLap_x2, oLap_y1, oLap_y2, cube1.z1, oLap_z1 - 1))
    if oLap_z2 < cube1.z2:
        result.append(Cube(1, oLap_x1, oLap_x2, oLap_y1, oLap_y2, oLap_z2 + 1, cube1.z2))

    return result

allCubes = []

for line in cuboid:
    newCube = Cube(line[0], line[1], line[2], line[3], line[4], line[5], line[6])
    
    newCubes = [newCube]
    if newCube.onOff == 1:
        for existingCube in allCubes[:]:
            for subCube in newCubes[:]:
                newCubes.remove(subCube)
                newCubes.extend(subtract(subCube, existingCube))
        allCubes.extend(newCubes)
    else:
        updatedCubes = []
        for existingCube in allCubes:
            updatedCubes.extend(subtract(existingCube, newCube))
        allCubes = updatedCubes

count = sum(vol(cube) for cube in allCubes if cube.onOff == 1)

print(count)
