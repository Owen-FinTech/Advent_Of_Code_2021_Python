input_string = '''''' # Insert your puzzle input between the triple quotes

input = input_string.split('\n')

oxygen_input = input.copy()

while len(oxygen_input) > 1:
    for i in range(0, len(oxygen_input[0])):
        zero_count = 0
        one_count = 0
        for j in range(0, len(oxygen_input)):
            if oxygen_input[j][i] == '0':
                zero_count += 1
            else:
                one_count += 1
        temp = []
        if one_count >= zero_count:
            for j in range(0, len(oxygen_input)):
                if oxygen_input[j][i] == '1':
                    temp.append(oxygen_input[j])
        else:
            for j in range(0, len(oxygen_input)):
                if oxygen_input[j][i] == '0':
                    temp.append(oxygen_input[j])
        oxygen_input = temp.copy()
        if len(oxygen_input) < 2:
            break

scrubber_input = input.copy()

while len(scrubber_input) > 1:
    for i in range(0, len(scrubber_input[0])):
        zero_count = 0
        one_count = 0
        for j in range(0, len(scrubber_input)):
            if scrubber_input[j][i] == '0':
                zero_count += 1
            else:
                one_count += 1
        temp = []
        if zero_count <= one_count:
            for j in range(0, len(scrubber_input)):
                if scrubber_input[j][i] == '0':
                    temp.append(scrubber_input[j])
        else:
            for j in range(0, len(scrubber_input)):
                if scrubber_input[j][i] == '1':
                    temp.append(scrubber_input[j])
        scrubber_input = temp.copy()
        if len(scrubber_input) < 2:
            break


result = int(oxygen_input[0], 2) * int(scrubber_input[0], 2) 

print('result:', result)

