#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div

nb_args = len(sys.argv) - 1
ops = ["+", "-", "*", "/"]

if __name__ == "__main__":
    if nb_args != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    if sys.argv[2] not in ops:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])
    op = sys.argv[2]
    result = (
        add(a, b) if op == "+" else
        sub(a, b) if op == "-" else
        mul(a, b) if op == "*" else
        div(a, b) if op == "/" else None
    )
    print("{} {} {}  = {}".format(a, op, b, result))
