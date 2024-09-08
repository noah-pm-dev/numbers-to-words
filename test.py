big_number_roots = {
    11: "Decillion",
    21: "Vigintillion",
    31: "Trigintillion"
}

for i in big_number_roots:
    try:
        print('a ', i)
        print(11 in range(i, i + 10))
    except:
        print('b')
        break