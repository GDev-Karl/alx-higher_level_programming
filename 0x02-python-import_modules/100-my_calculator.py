#!/usr/bin/python3
from sys import argv
from calculator_1 import add, sub, mul, div

nb_args = len(argv) - 1
ops = ["+", "-", "*", "/"]

if __name__ == "__main__":
    if nb_args < 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    elif argv[2] not in ops:
        print("Unknown operator. Available operators: +, -, * and /")
    else:
        a = argv[1]
        b = argv[3]
        op = argv[2]
        result = (
            add(a, b) if op == "+" else
            sub(a, b) if op == "-" else
            mul(a, b) if op == "*" else
            div(a, b) if op == "/" else None
        )
        print("{} {} {}  = {}".format(a, op, b, result))
