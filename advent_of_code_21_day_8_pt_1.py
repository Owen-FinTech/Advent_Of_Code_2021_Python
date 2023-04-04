input_string = '''''' # Insert your puzzle input between the triple quotes

input = input_string.split('\n')

for i in range(0, len(input)):
    input[i] = input[i].split(' ')

known_numbers = 0

for i in range(0, len(input)):
    for j in range(11, 15):
        if (len(input[i][j]) == 2 or len(input[i][j]) == 3 or
        len(input[i][j]) == 4 or len(input[i][j]) == 7):
            known_numbers += 1

result = known_numbers

print('result:', result)
