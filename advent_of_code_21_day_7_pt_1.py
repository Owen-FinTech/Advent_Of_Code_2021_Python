input_string = '''''' # Insert your puzzle input between the triple quotes

input = input_string.split(',')

for i in range(0, len(input)):
    input[i] = int(input[i])

least_fuel = 0

for i in range(min(input), max(input) + 1):
    fuel = 0
    for j in range(0, len(input)):
        if input[j] < i:
            fuel += (i - input[j])
        elif input[j] > 1:
            fuel += (input[j] - i)
    if least_fuel == 0:
        least_fuel = fuel
    else:
        if fuel < least_fuel:
            least_fuel = fuel

result = least_fuel

print('result:', result)
