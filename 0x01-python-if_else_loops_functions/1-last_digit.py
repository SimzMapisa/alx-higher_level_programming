#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

last_digit = 0
if (number < 0):
    last_digit = abs(number) % 10
    last_digit = -last_digit
elif (number > 0):
    last_digit = number % 10
else:
    last_digit = 0

if (last_digit > 5):
    print("Last digit of %d is %d and is greater than 5" %
          (number, last_digit))
elif (last_digit < 6 and last_digit != 0):
    print("Last digit of %d is %d and is less than 6 and not 0" %
          (number, last_digit))
elif (last_digit == 0):
    print("Last digit of %d is %d and is 0" % (number, last_digit))
