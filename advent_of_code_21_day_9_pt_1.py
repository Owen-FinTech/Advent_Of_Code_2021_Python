input_string = '''''' # Insert your puzzle input between the triple quotes

input = input_string.split('\n')

for i in range(0, len(input)):
    input[i] = list(input[i])
    for j in range(0, len(input[i])):
        input[i][j] = int(input[i][j])

risk_list = []

for i in range(0, len(input)):
    for j in range(0, len(input[i])):
        if i == 0 and j == 0:
            if input[i][j] < input[i][j + 1] and input[i][j] < input[i + 1][j]:
                risk_list.append(input[i][j] + 1)
        elif i == 0 and j == len(input[i]) - 1:
            if input[i][j] < input[i][j - 1] and input[i][j] < input[i + 1][j]:
                risk_list.append(input[i][j] + 1)
        elif i == len(input) - 1 and j == 0:
            if input[i][j] < input[i][j + 1] and input[i][j] < input[i - 1][j]:
                risk_list.append(input[i][j] + 1)
        elif i == len(input) - 1 and j == len(input[i]) - 1:
            if input[i][j] < input[i][j - 1] and input[i][j] < input[i - 1][j]:
                risk_list.append(input[i][j] + 1)
        elif i == 0 and j > 0 and j < len(input[i]) - 1:
            if input[i][j] < input[i][j - 1] and input[i][j] < input[i][j + 1] and input[i][j] < input[i + 1][j]:
                risk_list.append(input[i][j] + 1)
        elif i > 0 and i < len(input) - 1 and j == len(input[i]) - 1:
            if input[i][j] < input[i][j - 1] and input[i][j] < input[i + 1][j] and input[i][j] < input[i - 1][j]:
                risk_list.append(input[i][j] + 1)
        elif i == len(input) - 1 and j > 0 and j < len(input[i]) - 1:
            if input[i][j] < input[i][j - 1] and input[i][j] < input[i][j + 1] and input[i][j] < input[i - 1][j]:
                risk_list.append(input[i][j] + 1)
        elif i > 0 and i < len(input) - 1 and j == 0:
            if input[i][j] < input[i][j + 1] and input[i][j] < input[i + 1][j] and input[i][j] < input[i - 1][j]:
                risk_list.append(input[i][j] + 1)
        else:
            if input[i][j] < input[i][j + 1] and input[i][j] < input[i][j - 1] and input[i][j] < input[i + 1][j] and input[i][j] < input[i - 1][j]:
                risk_list.append(input[i][j] + 1)

result = sum(risk_list)

print('result:', result)
        
