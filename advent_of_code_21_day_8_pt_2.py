input_string = '''''' # Insert your puzzle input between the triple quotes

input = input_string.split('\n')

for i in range(0, len(input)):
    input[i] = input[i].split(' ')
    for j in range(0, len(input[i])):
        input[i][j] = [input[i][j], '_']

for i in range(0, len(input)):
    for j in range(0, 10):
        if len(input[i][j][0]) == 2:
            input[i][j][1] = '1'
            one = input[i][j][0]
        elif len(input[i][j][0]) == 3:
            input[i][j][1] = '7'
        elif len(input[i][j][0]) == 4:
            input[i][j][1] = '4'
            four = input[i][j][0]
        elif len(input[i][j][0]) == 7:
            input[i][j][1] = '8'
    for j in range(0, 10):
        if (len(input[i][j][0]) == 5 and one[0] in input[i][j][0] and 
        one[1] in input[i][j][0]):
            input[i][j][1] = '3'
            three = input[i][j][0]
    for j in range(0, 10):
        if len(input[i][j][0]) == 6:
            nine_count = 0
            for k in range(0, len(three)):
                if three[k] in input[i][j][0]:
                    nine_count += 1
            if nine_count == 5:
                input[i][j][1] = '9'
                nine = input[i][j][0]
                for k in range(0, len(nine)):
                    if nine[k] not in three:
                        top_left = nine[k]
    for j in range(0, len(four)):
        if four[j] not in one and four[j] not in top_left:
            middle = four[j]
    for j in range(0, 10):
        if len(input[i][j][0]) == 6 and middle not in input[i][j][0]:
            input[i][j][1] = '0'
            zero = input[i][j][0]
    for j in range(0, 10):
        if len(input[i][j][0]) == 6 and input[i][j][0] != zero and input[i][j][0] != nine:
            input[i][j][1] = '6'
    for j in range(0, 10):
        if len(input[i][j][0]) == 5 and input[i][j][0] != three and top_left in input[i][j][0]:
            input[i][j][1] = '5'
    for j in range(0, 10):
        if len(input[i][j][0]) == 5 and input[i][j][1] == '_':
            input[i][j][1] = '2'

for i in range(0, len(input)):
    for j in range(11, 15):
        for k in range(0, 10):
            if len(input[i][j][0]) == len(input[i][k][0]):
                count = 0
                for l in range(0, len(input[i][j][0])):
                    if input[i][j][0][l] in input[i][k][0]:
                        count += 1
                if count == len(input[i][j][0]):
                    input[i][j][1] = input[i][k][1]

result = 0

for i in range(0, len(input)):
    result += int(input[i][11][1] + input[i][12][1] + input[i][13][1] + input[i][14][1])

print('result:', result)