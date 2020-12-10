#!/usr/bin/python3


def my_function():
    import hidden_4
    for count in dir(hidden_4):
        if count[0] != "_" and count[1] != "_":
            print(count)


if __name__ == "__main__":
    my_function()