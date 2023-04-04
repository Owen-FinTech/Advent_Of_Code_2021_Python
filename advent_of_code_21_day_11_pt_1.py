import copy

input_string = '''''' # Insert your puzzle input between the triple quotes

input = input_string.split('\n')

for i in range(0, len(input)):
    input[i] = list(input[i])
    for j in range(0, len(input[i])):
        input[i][j] = int(input[i][j])

step = 0 
flashes = 0

temp = copy.deepcopy(input)

while step < 100:
    for i in range(0, len(temp)):
        for j in range(0, len(temp[i])):
            temp[i][j] += 1
            if temp[i][j] > 9:
                temp[i][j] = 0
    progress = True
    while progress == True:
        changes = 0
        for i in range(0, len(temp)):
            for j in range(0, len(temp[i])):
                if temp[i][j] == 0:
                    temp[i][j] = 0
                else:
                    if i == 0 and j == 0 and temp[i][j] != 0:
                        add = 0
                        if temp[i][j + 1] == 0:
                            add += 1
                        if temp[i + 1][j] == 0:
                            add += 1
                        if temp[i + 1][j + 1] == 0:
                            add += 1
                        if temp[i][j] != input[i][j] + add + 1:
                            temp[i][j] = input[i][j] + add + 1
                            if temp[i][j] > 9:
                                temp[i][j] = 0
                            changes += 1
                    elif i == 0 and j == len(temp[0]) - 1 and temp[i][j] != 0:
                        add = 0
                        if temp[i][j - 1] == 0:
                            add += 1
                        if temp[i + 1][j] == 0:
                            add += 1
                        if temp[i + 1][j - 1] == 0:
                            add += 1
                        if temp[i][j] != input[i][j] + add + 1:
                            temp[i][j] = input[i][j] + add + 1
                            if temp[i][j] > 9:
                                temp[i][j] = 0
                            changes += 1
                    elif i == len(temp) - 1 and j == len(temp[0]) - 1 and temp[i][j] != 0:
                        add = 0
                        if temp[i][j - 1] == 0:
                            add += 1
                        if temp[i - 1][j] == 0:
                            add += 1
                        if temp[i - 1][j - 1] == 0:
                            add += 1
                        if temp[i][j] != input[i][j] + add + 1:
                            temp[i][j] = input[i][j] + add + 1
                            if temp[i][j] > 9:
                                temp[i][j] = 0
                            changes += 1
                    elif i == len(temp) - 1 and j == 0 and temp[i][j] != 0:
                        add = 0
                        if temp[i][j + 1] == 0:
                            add += 1
                        if temp[i - 1][j] == 0:
                            add += 1
                        if temp[i - 1][j + 1] == 0:
                            add += 1
                        if temp[i][j] != input[i][j] + add + 1:
                            temp[i][j] = input[i][j] + add + 1
                            if temp[i][j] > 9:
                                temp[i][j] = 0
                            changes += 1
                    elif i == 0 and j > 0 and j < len(temp[0]) - 1 and temp[i][j] != 0:
                        add = 0
                        if temp[i][j + 1] == 0:
                            add += 1
                        if temp[i][j - 1] == 0:
                            add += 1
                        if temp[i + 1][j + 1] == 0:
                            add += 1
                        if temp[i + 1][j] == 0:
                            add += 1
                        if temp[i + 1][j - 1] == 0:
                            add += 1
                        if temp[i][j] != input[i][j] + add + 1:
                            temp[i][j] = input[i][j] + add + 1
                            if temp[i][j] > 9:
                                temp[i][j] = 0
                            changes += 1
                    elif i > 0 and i < len(temp) - 1 and j == len(temp[0]) - 1 and temp[i][j] != 0:
                        add = 0
                        if temp[i + 1][j] == 0:
                            add += 1
                        if temp[i - 1][j] == 0:
                            add += 1
                        if temp[i][j - 1] == 0:
                            add += 1
                        if temp[i - 1][j - 1] == 0:
                            add += 1
                        if temp[i + 1][j - 1] == 0:
                            add += 1
                        if temp[i][j] != input[i][j] + add + 1:
                            temp[i][j] = input[i][j] + add + 1
                            if temp[i][j] > 9:
                                temp[i][j] = 0
                            changes += 1
                    elif i == len(temp) - 1 and j > 0 and j < len(temp[0]) - 1 and temp[i][j] != 0:
                        add = 0
                        if temp[i][j + 1] == 0:
                            add += 1
                        if temp[i][j - 1] == 0:
                            add += 1
                        if temp[i - 1][j + 1] == 0:
                            add += 1
                        if temp[i - 1][j] == 0:
                            add += 1
                        if temp[i - 1][j - 1] == 0:
                            add += 1
                        if temp[i][j] != input[i][j] + add + 1:
                            temp[i][j] = input[i][j] + add + 1
                            if temp[i][j] > 9:
                                temp[i][j] = 0
                            changes += 1
                    elif i > 0 and i < len(temp) - 1 and j == 0 and temp[i][j] != 0:
                        add = 0
                        if temp[i + 1][j] == 0:
                            add += 1
                        if temp[i - 1][j] == 0:
                            add += 1
                        if temp[i][j + 1] == 0:
                            add += 1
                        if temp[i - 1][j + 1] == 0:
                            add += 1
                        if temp[i + 1][j + 1] == 0:
                            add += 1
                        if temp[i][j] != input[i][j] + add + 1:
                            temp[i][j] = input[i][j] + add + 1
                            if temp[i][j] > 9:
                                temp[i][j] = 0
                            changes += 1
                    elif i > 0 and i < len(temp) - 1 and j > 0 and j < len(temp[0]) - 1 and temp[i][j] != 0:
                        add = 0
                        if temp[i + 1][j] == 0:
                            add += 1
                        if temp[i - 1][j] == 0:
                            add += 1
                        if temp[i][j + 1] == 0:
                            add += 1
                        if temp[i - 1][j + 1] == 0:
                            add += 1
                        if temp[i + 1][j + 1] == 0:
                            add += 1
                        if temp[i][j - 1] == 0:
                            add += 1
                        if temp[i - 1][j - 1] == 0:
                            add += 1
                        if temp[i + 1][j - 1] == 0:
                            add += 1
                        if temp[i][j] != input[i][j] + add + 1:
                            temp[i][j] = input[i][j] + add + 1
                            if temp[i][j] > 9:
                                temp[i][j] = 0
                            changes += 1
        if changes == 0:
            progress = False
            break
    input = copy.deepcopy(temp)
    for i in range(0, len(input)):
        for j in range(0, len(input[i])):
            if input[i][j] == 0:
                flashes += 1
    step += 1
    if step == 100:
        break

result = flashes

print('result:', result)



