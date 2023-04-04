input_string = '''''' # Insert your puzzle input between the triple quotes

input = input_string.split('\n')

for i in range(0, len(input)):
    input[i] = input[i].split(' ')
    input[i][1] = int(input[i][1])

horizontal = 0
depth = 0
aim = 0

for i in range(0, len(input)):
    if input[i][0] == 'forward':
        horizontal += input[i][1]
        depth += (input[i][1] * aim)
    elif input[i][0] == 'down':
        aim += input[i][1]
    else:
        aim -= input[i][1]

result = horizontal * depth

print('result:', result)