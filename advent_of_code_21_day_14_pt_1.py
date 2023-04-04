template = '''''' # Insert the frist part of the puzzle input between the triple quotes

insertion_string = '''''' # Insert the second part of the puzzle input between the triple quotes

insertion = insertion_string.split('\n')

for i in range(0, len(insertion)):
    insertion[i] = insertion[i].split(' ')

step = 0

while step < 10:
    insert_list = []
    for i in range(0, len(template) - 1):
        for j in range(0, len(insertion)):
            if template[i:i + 2] == insertion[j][0]:
                insert_list.append([i + 1, insertion[j][2]])
    for i in range(0, len(insert_list)):
        template = template[:insert_list[i][0] + i] + insert_list[i][1] + template[insert_list[i][0] + i:]
    step += 1

occurances = {}
occurances_keys = occurances.keys()

for i in range(0, len(template)):
    if template[i] in occurances_keys:
        occurances[template[i]] += 1
    else:
        occurances[template[i]] = 1
    occurances_keys = occurances.keys()

occurances_values = occurances.values()

result = max(occurances_values) - min(occurances_values)

print('result:', result)

