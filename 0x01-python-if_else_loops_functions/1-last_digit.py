#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
str0 = 'Last digit of'
str1 = 'and is greater than 5'
str2 = 'and is 0'
str3 = 'and is less than 6 and not 0'
last_digit = int(str(number)[-1])
if last_digit > 5:
    print('{} {:d} is {:d} {}'.format(str0, number ,last_digit, str1))
elif last_digit == 0:
    print('{} {:d} is {:d} {}'.format(str0, number ,last_digit, str2))
elif last_digit < 6 | last_digit != 0:
    print('{} {:d} is {:d} {}'.format(str0, number ,last_digit, str3))
