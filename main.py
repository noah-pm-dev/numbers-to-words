from sys import stdout

def convert_two_digits(digits):
    if digits[0] == '1':
        if digits[1] == '1':
            return "Eleven"
        elif digits[1] == '2':
            return "Twelve"
        elif digits[1] == '0':
            return "Ten"
        else:
            return number_words[digits[1]][1] + 'een'
    elif digits[0] == '0':
        return number_words[digits[1]][0]
    else:
        return number_words[digits[0]][1] + 'y ' + number_words[digits[1]][0]


big_numbers = {
    21: "Vigintillion",
    20: "Novemdecillion",
    19: "Octodecillion",
    18: "Septendecillion",
    17: "Sexdecillion",
    16: "Quindecillion",
    15:	"Quattuordecillion",
    14: "Tredecillion",
    13: "Duodecillion",
    12: "Undecillion",
    11: "Decillion",
    10: "Nonillion",
    9:  "Octillion",
    8:  "Septillion",
    7:  "Sextillion",
    6:  "Quintillion",
    5:  "Quadrillion",
    4:  "Trillion",
    3:  "Billion",
    2:  "Million",
    1:  "Thousand"
}
number_words = {
    '0': [''],
    '1': ["One"],
    '2': ["Two", "Twent"],
    '3': ["Three", "Thirt"],
    '4': ["Four", "Fort"],
    '5': ["Five", "Fift"],
    '6': ["Six", "Sixt"],
    '7': ["Seven", "Sevent"],
    '8': ["Eight", "Eight"],
    '9': ["Nine", "Ninent"]
}

print("Input your number: ")
num = input()[::-1]
stdout.write("\033[32mResult:\033[0m\n")
split_num = [num[i:i+3][::-1] for i in range(0, len(num), 3)][::-1]

num_segments = len(split_num)

for i in split_num:
    num_segments -= 1
    if len(i) == 1:
        stdout.write(number_words[i][0])
    elif len(i) == 2:
        stdout.write(convert_two_digits(i))
    elif len(i) == 3:
        if i[0] != '0':
            stdout.write(number_words[i[0]][0] + ' Hundred and ' + convert_two_digits(i[1:]))
        else:
            stdout.write(convert_two_digits(i[1:]))
    
    try:
        stdout.write(' ' + big_numbers[num_segments] + ' ')
    except KeyError:
        break

print()