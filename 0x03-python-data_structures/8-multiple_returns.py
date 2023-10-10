#!/usr/bin/python3
def multiple_returns(sentence):
    str_len = len(sentence)
    if sentence:
        first_char = sentence[0]
    else:
        first_char = None

    return str_len, first_char
