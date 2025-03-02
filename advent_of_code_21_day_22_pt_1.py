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

allCubes = []
cubeCount = 0

for i in range(0, 101):
    allCubes.append([])

for cube in allCubes:
    for j in range(0, 101):
        cube.append([])

for cube in allCubes:
    for innerCube in cube:
        for k in range(0, 101):
            innerCube.append(0)

for line in cuboid:
    if line[1] <= 50 and line[2] >= -50:
        if line[1] < -50:
            line[1] = -50
        if line[2] > 50:
            line[2] = 50
        for i in range(line[1], line[2] + 1):
            if line[3] <= 50 and line[4] >= -50:
                if line[3] < -50:
                    line[3] = -50
                if line[4] > 50:
                    line[4] = 50
                for j in range(line[3], line[4] + 1):
                    if line[5] <= 50 and line[6] >= -50:
                        if line[5] < -50:
                            line[5] = -50
                        if line[6] > 50:
                            line[6] = 50
                        for k in range(line[5], line[6] + 1):
                            allCubes[i + 50][j + 50][k + 50] = line[0]

for cube in allCubes:
    for innerCube in cube:
        for onOff in innerCube:
            if onOff == 1:
                cubeCount += 1

print(cubeCount)

