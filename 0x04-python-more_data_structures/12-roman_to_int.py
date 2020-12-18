#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return 0
    dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    aux = roman_string
    sum = 0
    for i in range(len(roman_string)):
        if dic[aux[i]] > dic[aux[i - 1]] and i > 0:
            sum += dic[aux[i]] - (2 * dic[aux[i - 1]])
        else:
            sum += dic[aux[i]]
    return sum
