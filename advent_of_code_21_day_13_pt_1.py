input_string = '''''' # Insert the first part of the puzzle input between the triple quotes

fold_instructions = '''''' # Insert the second part of the puzzle input between the triple quotes

input = input_string.split('\n')

for i in range(0, len(input)):
    input[i] = input[i].split(',')
    for j in range(0, len(input[i])):
        input[i][j] = int(input[i][j])

fold = fold_instructions.split('\n')

for i in range(0, len(fold)):
    fold[i] = fold[i].split(' ')
    fold[i] = fold[i][2]

for i in range(0, len(fold)):
    fold[i] = fold[i].split('=')
    fold[i][1] = int(fold[i][1])

x_max = 0

for i in range(0, len(input)):
    if input[i][0] > x_max:
        x_max = input[i][0]

y_max = 0

for i in range(0, len(input)):
    if input[i][1] > y_max:
        y_max = input[i][1]

grid = []

for i in range(0, y_max + 1):
    grid.append([])

for i in range(0, len(grid)):
    for j in range(0, x_max + 1):
        grid[i].append('.')

for i in range(0, len(input)):
    grid[input[i][1]][input[i][0]] = '#'

if fold[0][0] == 'y':
    for i in range(fold[0][1] + 1, len(grid)):
        for j in range(0, len(grid[i])):
            if grid[i][j] == '#':
                grid[fold[0][1] - (i - fold[0][1])][j] = '#'
    for i in range(len(grid) - 1, fold[0][1] - 1, -1):
        del grid[i]
else:
    for i in range(0, len(grid)):
        for j in range(fold[0][1] + 1, len(grid[i])):
            if grid[i][j] == '#':
                grid[i][fold[0][1] - (j - fold[0][1])] = '#'
    for i in range(0, len(grid)):
        for j in range(len(grid[i]) - 1, fold[0][1] - 1, -1):
            del grid[i][j]

result = 0

for i in range(0, len(grid)):
    for j in range(0, len(grid[i])):
        if grid[i][j] == '#':
            result += 1

print('result:', result)





