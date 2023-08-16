#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    score = 0
    highest = ""
    for i in a_dictionary:
        if a_dictionary[i] > score:
            highest = i
            score = a_dictionary[i]
    return highest
