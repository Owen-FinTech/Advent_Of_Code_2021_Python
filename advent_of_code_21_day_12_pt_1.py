import copy

input_string = '''''' # Insert your puzzle input between the triple quotes

input = input_string.split('\n')

for i in range(0, len(input)):
    input[i] = input[i].split('-')

adj = {}

for i in range(0, len(input)):
    adj[input[i][0]] = []
    adj[input[i][1]] = []

for i in range(0, len(input)):
    adj[input[i][0]].append(input[i][1])
    adj[input[i][1]].append(input[i][0])

lower_visited = {}

for i in range(0, len(input)):
    for j in range(0, len(input[i])):
        if input[i][j][0] == input[i][j][0].lower():
            lower_visited[input[i][j]] = 0

lower_keys = lower_visited.keys()

options = [['start', lower_visited.copy()]]
options[0][1]['start'] = 1

paths = 0

while len(options) > 0:
    temp = []
    for i in range(0, len(options)):
        for j in range(0, len(adj[options[i][0]])):
            if adj[options[i][0]][j] in lower_keys:
                if options[i][1][adj[options[i][0]][j]] == 0:
                    new = copy.deepcopy(options[i])
                    new[0] = adj[options[i][0]][j]
                    new[1][adj[options[i][0]][j]] += 1
                    temp.append(new)
            else:
                new = copy.deepcopy(options[i])
                new[0] = adj[options[i][0]][j]
                temp.append(new)
    for i in range(len(temp) - 1, -1, -1):
        if temp[i][0] == 'end':
            del temp[i]
            paths += 1
    if len(temp) == 0:
        break
    options = copy.deepcopy(temp)

result = paths

print('result:', result)


