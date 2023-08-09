#!/usr/bin/python3
for i in range(48, 58):
    for j in range(48, 58):
        if i == j:
            continue
        if (i - j) < (j - i):
            print("{}{}".format(chr(i), chr(j)), end="")
            if i == 56 and j == 57:
                break
            print(", ", end="")
print()
