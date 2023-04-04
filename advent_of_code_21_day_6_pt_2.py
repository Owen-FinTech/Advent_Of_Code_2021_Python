input_string = '''''' # Insert your puzzle input between the triple quotes

input = input_string.split(',')

for i in range(0, len(input)):
    input[i] = int(input[i])

fish_dict = {'0': 0,
            '1': 0,
            '2': 0,
            '3': 0,
            '4': 0,
            '5': 0,
            '6': 0,
            '7': 0,
            '8': 0
            }

for i in range(0, len(input)):
    fish_dict[str(input[i])] += 1

days = 0

while days < 256:
    temp_dict = {'0': fish_dict['1'],
                '1': fish_dict['2'],
                '2': fish_dict['3'],
                '3': fish_dict['4'],
                '4': fish_dict['5'],
                '5': fish_dict['6'],
                '6': fish_dict['7'] + fish_dict['0'],
                '7': fish_dict['8'],
                '8': fish_dict['0']
                }
    fish_dict = temp_dict.copy()
    days += 1
    if days == 256:
        break

result = (fish_dict['0'] + fish_dict['1'] + fish_dict['2'] + 
        fish_dict['3'] + fish_dict['4']+ fish_dict['5'] + 
        fish_dict['6'] + fish_dict['7'] + fish_dict['8'])

print('result:', result)