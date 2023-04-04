input_string = '''''' # Insert your puzzle input between the triple quotes

input = input_string.split('\n')

points = 0
openers = ['(', '[', '{', '<']
closers = [')', ']', '}', '>']

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
                if input[i][j] == ')':
                    points += 3
                    break
                elif input[i][j] == ']':
                    points += 57
                    break
                elif input[i][j] == '}':
                    points += 1197
                    break
                else:
                    points += 25137
                    break

result = points

print('result:', result)
