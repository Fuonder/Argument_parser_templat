#!/usr/bin/env python3

import argparse
import string


def do_math(function: string, base: float, **kwargs) -> float:
    # PARSE INPUT
    # CALL FUNCTIONS
    #
    # my_pow(base, power, accuracy)

    print(f"Arguments:\n\tfunction - {function}\n\tbase - {base}")
    if function != "fact":
        for key, value in kwargs.items():
            print(f"\t{key} - {value}")
    else:
        pass
    pass


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog="My_math prog",
        description="This is a small math library",
        epilog="By User (C)(R) 2024",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument('function', choices=['pow', 'sqrt', 'fact'], help ='function to execute')
    parser.add_argument('-v', '--version', action='version', version='%(prog)s 1.0.0')

    parser.add_argument('base', type=float, help='base number')
    parser.add_argument('-p', '--power', type=float, help='second argument power or sqrt_base', default=None)
    parser.add_argument('-a', '--accuracy', type=int, help='calculation accuracy', default=8)

    aarg = vars(parser.parse_args())

    do_math(function=aarg['function'], base=aarg['base'], power=aarg['power'], accuracy=aarg['accuracy'])

