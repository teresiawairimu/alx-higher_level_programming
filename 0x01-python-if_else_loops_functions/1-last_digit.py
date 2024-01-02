#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
numeral = abs(number) % 10
if number < 0:
    numeral = -numeral
print("Last numeral of {} is {} and is ".format(number, numeral), end="")
if numeral > 5:
    print("greater than 5")
elif numeral == 0:
    print("0")
else:
    print("less than 6 and not 0")
