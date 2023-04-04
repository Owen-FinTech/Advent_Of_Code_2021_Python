input_string = '''''' # Insert your puzzle input between the triple quotes

input = input_string.split('\n')

for i in range(0, len(input)):
    input[i] = int(input[i])

count = 0

for i in range(2, len(input) - 1):
    if (input[i] + input[i - 1] + input[i + 1]) > (input[i] + input[i - 1] + input[i - 2]):
        count += 1

print("count:", count)