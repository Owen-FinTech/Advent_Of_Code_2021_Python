import math

input_string = '''''' # Insert your puzzle input between the triple quotes

input = input_string.split('\n')

points = 0
openers = ['(', '[', '{', '<']
closers = [')', ']', '}', '>']

delete_list = []

for i in range(0, len(input)):
    for j in range(0, len(input[i])):
        if input[i][j] in closers:
            tally = {'(': 0, '[': 0, '{': 0, '<': 0, ')': 0, ']': 0, '}': 0, '>': 0}
            for k in range(j, -1, -1):
                tally[input[i][k]] += 1
                if ((input[i][j] == closers[0] and input[i][k] == openers[0] and tally[input[i][j]] == tally[input[i][k]]) or 
                (input[i][j] == closers[1] and input[i][k] == openers[1] and tally[input[i][j]] == tally[input[i][k]]) or
                (input[i][j] == closers[2] and input[i][k] == openers[2] and tally[input[i][j]] == tally[input[i][k]]) or
                (input[i][j] == closers[3] and input[i][k] == openers[3] and tally[input[i][j]] == tally[input[i][k]])):
                    break
            if (tally['('] != tally[')'] or tally['['] != tally[']'] or 
            tally['{'] != tally['}'] or tally['<'] != tally['>']):
                delete_list.append(i)
                break

for i in range(len(delete_list) - 1, -1, -1):
    del input[delete_list[i]]

additional_list = []

for i in range(0, len(input)):
    tally = {'(': 0, '[': 0, '{': 0, '<': 0, ')': 0, ']': 0, '}': 0, '>': 0}
    additional = []
    for j in range(len(input[i]) - 1, -1, -1):
        tally[input[i][j]] += 1
        if tally['('] > tally[')']:
            additional.append(')')
            tally[')'] += 1
        elif tally['['] > tally[']']:
            additional.append(']')
            tally[']'] += 1
        elif tally['{'] > tally['}']:
            additional.append('}')
            tally['}'] += 1
        elif tally['<'] > tally['>']:
            additional.append('>')
            tally['>'] += 1
    additional_list.append(additional)

score_list = []

for i in range(0, len(additional_list)):
    score = 0
    for j in range(0, len(additional_list[i])):
        score *= 5
        if additional_list[i][j] == ')':
            score += 1
        elif additional_list[i][j] == ']':
            score += 2
        elif additional_list[i][j] == '}':
            score += 3
        else:
            score += 4
    score_list.append(score)

score_list.sort()

result = score_list[math.floor(len(score_list) / 2)]

print('result:', result)

        
