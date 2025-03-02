input_string = '''''' # Insert your puzzle input between the triple quotes

p1Pos: int
p2Pos: int
splitString = input_string.split("\n")

for i in range(len(splitString)):
    for j in range(len(splitString[i]) - 1, -1, -1):
        if splitString[i][j] == " ":
            if i == 0:
                p1Pos = int(splitString[i][j + 1:])
                break
            else:
                p2Pos = int(splitString[i][j + 1:])
                break

p1Score = 0
p2Score = 0
dice = 1
rolls = 0
move = 0

def movement(move, dice, rolls):
    move = 0
    for i in range(0, 3):
        move += dice
        rolls += 1
        dice = (dice % 100) + 1
    return move, dice, rolls
        

while p1Score < 1000 and p2Score < 1000:
    move, dice, rolls = movement(move, dice, rolls)
    p1Pos = (((p1Pos - 1) + move) % 10) + 1
    p1Score += p1Pos

    if p1Score >= 1000:
        break

    move, dice, rolls = movement(move, dice, rolls)
    p2Pos = (((p2Pos - 1) + move) % 10) + 1
    p2Score += p2Pos

if p1Score >= 1000:
    print("result: ", rolls * p2Score)
else:
    print("result: ", rolls * p1Score)

    

