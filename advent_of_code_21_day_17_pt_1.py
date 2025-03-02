input_string = '''''' # Insert your puzzle input between the triple quotes

x_lower_str = ""
in_num = False

for i in input_string:
    if i == ".":
        break

    if in_num:
        x_lower_str += i
    
    if i == "=":
        in_num = True 

x_lower = int(x_lower_str)

x_upper_str = ""
in_num = False
period_count = 0

for i in input_string:
    if i == ".":
        period_count += 1
    elif i == ",":
        break

    if in_num:
        x_upper_str += i
    
    if period_count == 2:
        in_num = True
    
x_upper = int(x_upper_str)

y_lower_str = ""
in_num = False
period_count = 0
equals_count = 0

for i in input_string:
    if i == ".":
        period_count += 1
    elif i == "=":
        equals_count += 1

    if period_count == 3:
        break

    if in_num:
        y_lower_str += i

    if equals_count == 2:
        in_num = True
       
y_lower = int(y_lower_str)

y_upper_str = ""
in_num = False
period_count = 0

for i in input_string:
    if i == ".":
        period_count += 1

    if in_num:
        y_upper_str += i

    if period_count == 4:
        in_num = True
       
y_upper = int(y_upper_str)


y_max_valid = 0

for x_vel in range(0, x_upper + 1):
    for y_vel in range(0, 0 - y_lower):
        x = 0
        y = 0
        round = 0
        y_max = 0

        while x <= x_upper and y >= y_lower:
            if (x_vel - round) > 0:
                x += (x_vel - round)
            
            y += (y_vel - round)

            if y > y_max:
                    y_max = y

            if x >= x_lower and x <= x_upper and y <= y_upper and y >= y_lower:
                if y_max > y_max_valid:
                    y_max_valid = y_max
                break

            round += 1
            
print("result: ", str(y_max_valid))


