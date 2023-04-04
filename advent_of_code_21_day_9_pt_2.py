input_string = '''''' # Insert your puzzle input between the triple quotes

input = input_string.split('\n')

for i in range(0, len(input)):
    input[i] = list(input[i])
    for j in range(0, len(input[i])):
        input[i][j] = int(input[i][j])

low_points = []

for i in range(0, len(input)):
    for j in range(0, len(input[i])):
        if i == 0 and j == 0:
            if input[i][j] < input[i][j + 1] and input[i][j] < input[i + 1][j]:
                low_points.append([i, j])
        elif i == 0 and j == len(input[i]) - 1:
            if input[i][j] < input[i][j - 1] and input[i][j] < input[i + 1][j]:
                low_points.append([i, j])
        elif i == len(input) - 1 and j == 0:
            if input[i][j] < input[i][j + 1] and input[i][j] < input[i - 1][j]:
                low_points.append([i, j])
        elif i == len(input) - 1 and j == len(input[i]) - 1:
            if input[i][j] < input[i][j - 1] and input[i][j] < input[i - 1][j]:
                low_points.append([i, j])
        elif i == 0 and j > 0 and j < len(input[i]) - 1:
            if input[i][j] < input[i][j - 1] and input[i][j] < input[i][j + 1] and input[i][j] < input[i + 1][j]:
                low_points.append([i, j])
        elif i > 0 and i < len(input) - 1 and j == len(input[i]) - 1:
            if input[i][j] < input[i][j - 1] and input[i][j] < input[i + 1][j] and input[i][j] < input[i - 1][j]:
                low_points.append([i, j])
        elif i == len(input) - 1 and j > 0 and j < len(input[i]) - 1:
            if input[i][j] < input[i][j - 1] and input[i][j] < input[i][j + 1] and input[i][j] < input[i - 1][j]:
                low_points.append([i, j])
        elif i > 0 and i < len(input) - 1 and j == 0:
            if input[i][j] < input[i][j + 1] and input[i][j] < input[i + 1][j] and input[i][j] < input[i - 1][j]:
                low_points.append([i, j])
        else:
            if input[i][j] < input[i][j + 1] and input[i][j] < input[i][j - 1] and input[i][j] < input[i + 1][j] and input[i][j] < input[i - 1][j]:
                low_points.append([i, j])

sizes = []

for i in range(0, len(low_points)):
    basin = [low_points[i]]
    progress = True
    while progress == True:
        appended = 0
        temp = []
        for j in range(0, len(basin)):
            if basin[j][0] != 0:
                appendable = True
                for k in range(0, len(basin)):
                    if basin[j][0] - 1 == basin[k][0] and basin[j][1] == basin[k][1]:
                        appendable = False
                        break
                for k in range(0, len(temp)):
                    if basin[j][0] - 1 == temp[k][0] and basin[j][1] == temp[k][1]:
                        appendable = False
                        break
                if appendable == True and input[basin[j][0] - 1][basin[j][1]] < 9:
                    temp.append([basin[j][0] - 1, basin[j][1]])
                    appended += 1
            if basin[j][1] != len(input[0]) - 1:
                appendable = True
                for k in range(0, len(basin)):
                    if basin[j][0] == basin[k][0] and basin[j][1] + 1 == basin[k][1]:
                        appendable = False
                        break
                for k in range(0, len(temp)):
                    if basin[j][0] == temp[k][0] and basin[j][1] + 1 == temp[k][1]:
                        appendable = False
                        break
                if appendable == True and input[basin[j][0]][basin[j][1] + 1] < 9:
                    temp.append([basin[j][0], basin[j][1] + 1])
                    appended += 1
            if basin[j][0] != len(input) - 1:
                appendable = True
                for k in range(0, len(basin)):
                    if basin[j][0] + 1 == basin[k][0] and basin[j][1] == basin[k][1]:
                        appendable = False
                        break
                for k in range(0, len(temp)):
                    if basin[j][0] + 1 == temp[k][0] and basin[j][1] == temp[k][1]:
                        appendable = False
                        break
                if appendable == True and input[basin[j][0] + 1][basin[j][1]] < 9:
                    temp.append([basin[j][0] + 1, basin[j][1]])
                    appended += 1
            if basin[j][1] != 0:
                appendable = True
                for k in range(0, len(basin)):
                    if basin[j][0] == basin[k][0] and basin[j][1] - 1 == basin[k][1]:
                        appendable = False
                        break
                for k in range(0, len(temp)):
                    if basin[j][0] == temp[k][0] and basin[j][1] - 1 == temp[k][1]:
                        appendable = False
                        break
                if appendable == True and input[basin[j][0]][basin[j][1] - 1] < 9:
                    temp.append([basin[j][0], basin[j][1] - 1])
                    appended += 1
        if appended == 0:
            sizes.append(len(basin))
            progress = False
            break
        for j in range(0, len(temp)):
            basin.append(temp[j])

sizes.sort(reverse = True)

result = sizes[0] * sizes[1] * sizes[2]

print('result:', result)
        


            

