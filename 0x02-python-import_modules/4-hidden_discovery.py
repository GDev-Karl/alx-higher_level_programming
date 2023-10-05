#!/usr/bin/python3

if __name__ == "__main__":
    import hidden_4

    variables = dir(hidden_4)
    for var in variables:
        if var[:2] != "__":
            print(var)
