#!/usr/bin/python3
def multiple_returns(sentence):
    lengh = len(sentence)
    if lengh > 0:
        first_char = sentence[0]
    else:
        first_char = None
    return (lengh, first_char)
