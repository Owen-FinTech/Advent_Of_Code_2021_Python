import copy

template = '''''' # Insert the frist part of the puzzle input between the triple quotes

insertion_string = '''''' # Insert the second part of the puzzle input between the triple quotes

insertion = insertion_string.split('\n')

for i in range(0, len(insertion)):
    insertion[i] = insertion[i].split(' ')

pairs = {}
pairs_keys = list(pairs.keys())

for i in range(0, len(template) - 1):
    for j in range(0, len(insertion)):
        if template[i:i + 2] == insertion[j][0]:
            if template[i] + insertion[j][2] in pairs_keys:
                pairs[template[i] + insertion[j][2]] += 1
            else:
                pairs[template[i] + insertion[j][2]] = 1
            pairs_keys = list(pairs.keys())   
            if insertion[j][2] + template[i + 1] in pairs_keys:
                pairs[insertion[j][2] + template[i + 1]] += 1
            else:
                pairs[insertion[j][2] + template[i + 1]] = 1
            pairs_keys = list(pairs.keys())

step = 1

while step < 40:
    temp = {}
    temp_keys = list(temp.keys())
    for i in range(0, len(pairs_keys)):
        for j in range(0, len(insertion)):
            if pairs_keys[i] == insertion[j][0]:
                if pairs_keys[i][0] + insertion[j][2] in temp_keys:
                    temp[pairs_keys[i][0] + insertion[j][2]] += pairs[pairs_keys[i]]
                else:
                    temp[pairs_keys[i][0] + insertion[j][2]] = pairs[pairs_keys[i]]
                temp_keys = list(temp.keys())
                if insertion[j][2] + pairs_keys[i][1] in temp_keys:
                    temp[insertion[j][2] + pairs_keys[i][1]] += pairs[pairs_keys[i]]
                else:
                    temp[insertion[j][2] + pairs_keys[i][1]] = pairs[pairs_keys[i]]
                temp_keys = list(temp.keys())
                pairs[pairs_keys[i]] = 0
    for i in range(0, len(pairs_keys)):
        for j in range(0, len(temp_keys)):
            if pairs_keys[i] == temp_keys[j]:
                temp[temp_keys[j]] += pairs[pairs_keys[i]]
    pairs = copy.deepcopy(temp)
    pairs_keys = list(pairs.keys())
    step += 1

occurances = {}
occurances_keys = list(occurances.keys())

for i in range(0, len(pairs_keys)):
    if pairs_keys[i][0] in occurances_keys:
        occurances[pairs_keys[i][0]] += pairs[pairs_keys[i]]
    else:
        occurances[pairs_keys[i][0]] = pairs[pairs_keys[i]]
    occurances_keys = list(occurances.keys())

occurances[template[-1]] += 1

occurances_values = list(occurances.values())

result = max(occurances_values) - min(occurances_values)

print('result:', result)







