input_string = '''''' # Insert your puzzle input between the triple quotes

input = input_string.split('\n')

for i in range(0, len(input)):
    input[i] = input[i].split(' ')
    for j in range(0, len(input[i])):
        input[i][j] = input[i][j].split(',')
    del input[i][1]

for i in range(0, len(input)):
    for j in range(0, len(input[i])):
        for k in range(0, len(input[i][j])):
            input[i][j][k] = int(input[i][j][k])

for i in range(len(input) - 1, -1, -1):
    if input[i][0][0] != input[i][1][0] and input[i][0][1] != input[i][1][1]:
        del input[i]

x_max = 0
y_max = 0

for i in range(0, len(input)):
    for j in range(0, len(input[i])):
        if input[i][j][0] > x_max:
            x_max = input[i][j][0]
        if input[i][j][1] > y_max:
            y_max = input[i][j][1]

grid = []

for i in range(0, y_max + 1):
    grid.append([])

for i in range(0, len(grid)):
    for j in range(0, x_max + 1):
        grid[i].append('.')

for i in range(0, len(input)):
    if input[i][0][0] != input[i][1][0]:
        if input[i][0][0] < input[i][1][0]:
            for j in range(input[i][0][0], input[i][1][0] + 1):
                if grid[input[i][0][1]][j] == '.':
                    grid[input[i][0][1]][j] = '1'
                elif grid[input[i][0][1]][j] == '1':
                    grid[input[i][0][1]][j] = '2'
        else:
            for j in range(input[i][1][0], input[i][0][0] + 1):
                if grid[input[i][0][1]][j] == '.':
                    grid[input[i][0][1]][j] = '1'
                elif grid[input[i][0][1]][j] == '1':
                    grid[input[i][0][1]][j] = '2'
    elif input[i][0][1] != input[i][1][1]:
        if input[i][0][1] < input[i][1][1]:
            for j in range(input[i][0][1], input[i][1][1] + 1):
                if grid[j][input[i][0][0]] == '.':
                    grid[j][input[i][0][0]] = '1'
                elif grid[j][input[i][0][0]] == '1':
                    grid[j][input[i][0][0]] = '2'
        else:
            for j in range(input[i][1][1], input[i][0][1] + 1):
                if grid[j][input[i][0][0]] == '.':
                    grid[j][input[i][0][0]] = '1'
                elif grid[j][input[i][0][0]] == '1':
                    grid[j][input[i][0][0]] = '2'
    else:
        if grid[input[i][0][1]][input[i][0][0]] == '.':
            grid[input[i][0][1]][input[i][0][0]] = '1'
        elif grid[input[i][0][1]][input[i][0][0]] == '1':
            grid[input[i][0][1]][input[i][0][0]] = '2'

result = 0

for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == '2':
            result += 1

print('result:', result)