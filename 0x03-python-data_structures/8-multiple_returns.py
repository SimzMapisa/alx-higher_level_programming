#!/usr/bin/python3

def multiple_returns(sentence):
    if len(sentence) == 0:
        return(0, None)
    length =  len(sentence)
    first_char = sentence[0]
    res = (length, first_char)
    return(res)

