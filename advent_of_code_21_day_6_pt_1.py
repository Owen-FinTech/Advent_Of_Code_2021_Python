input_string = '''''' # Insert your puzzle input between the triple quotes

input = input_string.split(',')

for i in range(0, len(input)):
    input[i] = int(input[i])

days = 0

while days < 80:
    temp = []
    for i in range(0, len(input)):
        if input[i] == 0:
            temp.append(6)
            temp.append(8)
        else:
            temp.append(input[i] - 1)
    input = temp.copy()
    days += 1
    if days == 80:
        break

result = len(input)

print('result:', result)
