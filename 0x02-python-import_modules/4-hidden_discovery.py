#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    list = dir(hidden_4)
    for s in list:
        if s[:2] != "__":
            print("{}".format(s))
