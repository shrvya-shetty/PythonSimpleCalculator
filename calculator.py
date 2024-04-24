#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: cjeffcoa
"""

import math


def basic():
    # =============================================================================
    #     +     for a + b
    #     -     for a - b
    #     /     for a / b
    #     *     for a * b
    # =============================================================================

    op = input(
        'What kind of operation would you like to do?\
        \nChoose between "+, -, *, /" : ')

    a = int(input('Please type the first number: '))
    b = int(input('Please type the second number: '))

    if op == '+':
        return str(a) + ' ' + op + ' ' + str(b) + ' = ' + str(a + b)
    elif op == '-':
        return str(a) + ' ' + op + ' ' + str(b) + ' = ' + str(a - b)
    elif op == '*':
        return str(a) + ' ' + op + ' ' + str(b) + ' = ' + str(a * b)
    elif op == '/':
        if b == 0:
            return 'Error: Cannot be divided by 0'
        else:
            return str(a) + ' ' + op + ' ' + str(b) + ' = ' + str(a / b)
    else:
        return "Incorrect operator! Please select from the given options!"


def scientific():
    # =============================================================================
    #     ^     for a ^ b
    #     %     for a mod b
    #     r     for the bth root of a (a ^ (1/b))
    #     !     for a factorial
    #     sin   for sin(a) in radians
    #     cos   for cos(a) in radians
    #     tan   for tan(a) in radians
    #     ln    for ln(a) (log base e of a)
    # =============================================================================

    op = input(
        'What kind of operation would you like to do?\
        \nChoose between "^, r, %, !, sin, cos, tan, ln" : ')
    if op in '^r%':
        a = float(input('Please type the first number: '))
        b = float(input('Please type the second number: '))
        if op == '^':
            return str(a) + ' ' + op + ' ' + str(b) + ' = ' + str(a ** b)  # Exponentiation
        elif op == 'r':
            return str(a) + ' ' + op + ' ' + str(b) + ' = ' + str(a ** (1 / b))  # Root
        elif op == '%':
            return str(a) + ' ' + op + ' ' + str(b) + ' = ' + str(a % b)  # Modulus
    elif op == '!':
        a = int(input('Please type the number: '))
        result = 1
        for i in range(1, a + 1):
            result *= i
        return str(a) + ' ' + op + ' = ' + str(result)  # Factorial
    elif op in ['sin', 'cos', 'tan']:
        a = float(input('Please type the angle in radians: '))
        if op == 'sin':
            return 'sin(' + str(a) + ') = ' + str(math.sin(a))
        elif op == 'cos':
            return 'cos(' + str(a) + ') = ' + str(math.cos(a))
        elif op == 'tan':
            return 'tan(' + str(a) + ') = ' + str(math.tan(a))
    elif op == 'ln':
        a = float(input('Please type the number: '))
        return 'ln(' + str(a) + ') = ' + str(math.log(a))  # Natural logarithm
    else:
        return "Incorrect operator! Please select from the given options!"

   

        # What kind of operation would you like to do?        
#Choose between "^, r, %, !, sin, cos, tan, ln" : sin
#Please type the angle in radians: 1.5708
#sin(1.5708) = 0.9999999999932537


def main():  # Wrapper function

    print("""Choose a calculator
    1. Basic Calculator
    2. Scientific Calculator""")
    choice = int(input('Please choose as 1 or 2: '))

    if choice == 1:
        print(basic())
    elif choice == 2:
        print(scientific())
    else:
        print('Invalid choice! Please select between 1 and 2:')


if __name__ == '__main__':
    main()
