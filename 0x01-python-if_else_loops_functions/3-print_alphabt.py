#!/usr/bin/python3

# store the ascii code for the first charater 'a'
ascii_code = 97

while ascii_code <= 122:
    # 'e' is 101 and q is 113
    if ascii_code == 101 or ascii_code == 113:
        pass
    else:
        print("{:c}".format(ascii_code), end="")

    ascii_code = ascii_code + 1
