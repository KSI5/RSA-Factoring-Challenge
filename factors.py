#!/usr/bin/python3

import sys
import time


def factorize(num):
    '''Takes a number as input.
    Args:
        num: input integer.
    Return: A list of tuples, each containing a factorization pair (p, q).
    '''
    factors = []
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            factors.append((i, num // i))
    return factors


if __name__ == "__main__":
    '''Reads the input file.
    '''
    if len(sys.argv) != 2:
        print("Usage: factors <file>")
        exit()

    input_file = sys.argv[1]

    try:
        with open(input_file, 'r') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print("File not found")
        exit()

    start_time = time.time()

    '''loops over each line (which should contain one natural number per line),
        and calls factorize on each number.
        If factorize returns a list of factors,
        it prints the factorization in the desired format.
    '''
    for line in lines:
        num = int(line.strip())
        factors = factorize(num)
        if factors:
            for factor in factors:
                p, q = factor
                print(f"{num}={p}*{q}")

        '''If the elapsed time exceeds 5 seconds,
            the program exits with an error message.
        '''
        if time.time() - start_time > 5:
            print("Time limit exceeded")
            exit()

