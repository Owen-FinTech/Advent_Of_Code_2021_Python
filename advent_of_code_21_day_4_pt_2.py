input_numbers = '''''' # Insert the first part of the puzzle input between the triple quotes

input_boards = '''''' # Insert the second part of the puzzle input between the triple quotes

input_numbers = input_numbers.split(',')

for i in range(0, len(input_numbers)):
    input_numbers[i] = int(input_numbers[i])

input_boards = input_boards.split('\n\n')

for i in range(0, len(input_boards)):
    input_boards[i] = input_boards[i].split('\n')
    for j in range(0, len(input_boards[i])):
        input_boards[i][j] = input_boards[i][j].split(' ')

for i in range(0, len(input_boards)):
    for j in range(0, len(input_boards[i])):
        for k in range(len(input_boards[i][j]) - 1, -1, -1):
            if input_boards[i][j][k] == '':
                del input_boards[i][j][k]

for i in range(0, len(input_boards)):
    for j in range(0, len(input_boards[i])):
        for k in range(0, len(input_boards[i][j])):
            input_boards[i][j][k] = int(input_boards[i][j][k])

def play_game(input_boards):
    bingo = False
    while bingo == False:
        for i in range(0, len(input_numbers)):
            current_number = input_numbers[i]
            for j in range(0, len(input_boards)):
                for k in range(0, len(input_boards[j])):
                    for l in range(0, len(input_boards[j][k])):
                        if input_boards[j][k][l] == input_numbers[i]:
                            input_boards[j][k][l] = 'B'
            for j in range(0, len(input_boards)):
                current_board = j
                for k in range(0, len(input_boards[j])):
                    if (input_boards[j][k][0] == 'B'
                    and input_boards[j][k][1] == 'B'
                    and input_boards[j][k][2] == 'B'
                    and input_boards[j][k][3] == 'B'
                    and input_boards[j][k][4] == 'B'):
                        bingo = True
                        break
                if bingo == True:
                    break
            if bingo == True:
                    break
            for j in range(0, len(input_boards)):
                current_board = j
                for l in range(0, len(input_boards[j][0])):
                    if (input_boards[j][0][l] == 'B'
                    and input_boards[j][1][l] == 'B'
                    and input_boards[j][2][l] == 'B'
                    and input_boards[j][3][l] == 'B'
                    and input_boards[j][4][l] == 'B'):
                        bingo = True
                        break
                if bingo == True:
                    break
            if bingo == True:
                    break
    sum_total = 0
    for i in range(0, len(input_boards[current_board])):
        for j in range(0, len(input_boards[current_board][i])):
            if input_boards[current_board][i][j] != 'B':
                sum_total += input_boards[current_board][i][j]
    result = current_number * sum_total
    del input_boards[current_board]
    return result
    
while len(input_boards) != 0:
    result = play_game(input_boards)
    if len(input_boards) == 0:
        break

print('result:', result)