input_string = '''''' # Insert your puzzle input between the triple quotes

input = input_string.split('\n')

gamma = ''
epsilon = ''

for i in range(0, len(input[0])):
    zero_count = 0
    one_count = 0
    for j in range(0, len(input)):
        if input[j][i] == '0':
            zero_count += 1
        else:
            one_count += 1
    if zero_count > one_count:
        gamma += '0'
        epsilon += '1'
    else:
        gamma += '1'
        epsilon += '0'

result = int(gamma, 2) * int(epsilon, 2)

print('result:', result)

