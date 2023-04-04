input_string = '''''' # Insert your puzzle input between the triple quotes

decoded_bin = ''

for i in range(len(input_string)):
    if input_string[i] == '0':
        decoded_bin += '0000'
    elif input_string[i] == '1':
        decoded_bin += '0001'
    elif input_string[i] == '2':
        decoded_bin += '0010'
    elif input_string[i] == '3':
        decoded_bin += '0011'
    elif input_string[i] == '4':
        decoded_bin += '0100'
    elif input_string[i] == '5':
        decoded_bin += '0101'
    elif input_string[i] == '6':
        decoded_bin += '0110'
    elif input_string[i] == '7':
        decoded_bin += '0111'
    elif input_string[i] == '8':
        decoded_bin += '1000'
    elif input_string[i] == '9':
        decoded_bin += '1001'
    elif input_string[i] == 'A':
        decoded_bin += '1010'
    elif input_string[i] == 'B':
        decoded_bin += '1011'
    elif input_string[i] == 'C':
        decoded_bin += '1100'
    elif input_string[i] == 'D':
        decoded_bin += '1101'
    elif input_string[i] == 'E':
        decoded_bin += '1110'
    else:
        decoded_bin += '1111'

start = 0
version = 0

while start < len(decoded_bin) - 12:
    version += int(decoded_bin[start: start + 3], 2)

    type = int(decoded_bin[start + 3: start + 6], 2)

    new_start = start + 6

    finish = False

    if type == 4:
        while finish == False:
            if decoded_bin[new_start] == '1':
                last = False
            else:
                last = True
            new_start += 5
            if last == True:
                start = new_start
                finish = True
                break
    else:
        if decoded_bin[new_start] == '0':
            start = new_start + 16
        else:
            start = new_start + 12

print('version:', version)
