#!/usr/bin/python3

def print_last_digit(number):
    last_digit = 0
    if number < 0:
        last_digit = abs(number) % 10
        last_digit = -last_digit
    else:
        last_digit = number % 10

    return last_digit

