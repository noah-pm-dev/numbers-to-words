from sys import stdout

def convert_two_digits(digits):
    if digits[0] == "1":
        if digits[1] == "1":
            return "Eleven"
        elif digits[1] == "2":
            return "Twelve"
        elif digits[1] == "0":
            return "Ten"
        else:
            return number_words[digits[1]][1] + "een"
    elif digits[0] == "0" and digits[1] != "0":
        return number_words[digits[1]][0]
    else:
        if digits[1] == "0":
            return number_words[digits[0]][1] + "y"
        else:
            return number_words[digits[0]][1] + "y-" + number_words[digits[1]][0]



big_number_roots = {
    11: "llion",
    101: "Centillion"
}

big_number_prefixes = {
    "0": "",
    "1": "Deci",
    "2": "Viginti",
    "3": "Triginti",
    "4": "Quadraginti",
    "5": "Quinquaginti",
    "6": "Sexaginti",
    "7": "Septuaginti",
    "8": "Octoginti",
    "9": "Nonaginti"
}

big_number_prefixes_prefixes = {
    "0": "",
    "1": "Un",
    "2": "Duo",
    "3": "Tre",
    "4": "Quattuor",
    "5": "Quin",
    "6": "Sex",
    "7": "Septen",
    "8": "Octo",
    "9": "Novem",
}

big_numbers = {
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
    "1": ["One"],
    "2": ["Two", "Twent"],
    "3": ["Three", "Thirt"],
    "4": ["Four", "Fort"],
    "5": ["Five", "Fift"],
    "6": ["Six", "Sixt"],
    "7": ["Seven", "Sevent"],
    "8": ["Eight", "Eight"],
    "9": ["Nine", "Ninent"]
}

print("Input your number: ")
num = input()[::-1]
stdout.write("\033[32mResult:\033[0m\n")
split = [num[i:i+3][::-1] for i in range(0, len(num), 3)][::-1]

split_num = split[:]
for num, i in enumerate(split):
    if set(i) == {"0"}:
        split_num.pop(0)
    else:
        break


num_segments = len(split_num)

print(split_num)
for num, i in enumerate(split_num):
    num_segments -= 1
    
    if set(i) == {"0"}:
        continue
    if len(i) == 1:
        stdout.write(number_words[i][0])
    elif len(i) == 2:
        stdout.write(convert_two_digits(i))
    elif len(i) == 3:
        if i[0] != "0":
            if i[1:] != "00":   
                stdout.write(number_words[i[0]][0] + " Hundred and " + convert_two_digits(i[1:]))
            else:
                stdout.write(number_words[i[0]][0] + " Hundred")
        elif i[1] != "0":
            if num != 0:
                stdout.write("and " + convert_two_digits(i[1:]))
            else:
                stdout.write(convert_two_digits(i[1:]))
        elif i[2] != "0":
            stdout.write("and " + number_words[i[2]][0])
    
    if num_segments > 10:
        for i in big_number_roots:
            try:
                if num_segments in range(i, i + 90):
                    stdout.write(" " + big_number_prefixes_prefixes[str(num_segments - 1)[-2:][1:]] + big_number_prefixes[str(num_segments - 1)[-2:][:1]] + big_number_roots[i] + " ")
                    continue
            except KeyError:
                print("\033[33mwtf\033[0m")
    else:
        try:
            stdout.write(" " + big_numbers[num_segments] + " ")
        except KeyError:
            break


print()