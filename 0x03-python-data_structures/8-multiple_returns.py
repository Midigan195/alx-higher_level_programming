#!/usr/bin/python3
def multiple_returns(sentence):
    s = list(sentence)
    c1 = 0
    if len(s) == 0:
        c1 = None
    else:
        c1 = s[0]
    text = (len(s), c1)
    return text
