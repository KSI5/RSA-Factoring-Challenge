#!/usr/bin/python3

import sys
import time
import math

def factorize(number):
    '''Takes a number as input.
    Args:
        number: input integer.
    Returns: A list of tuples, each containing a factorization pair (p, q).
    '''
    factors = []
    limit = math.isqrt(number) + 1
    for i in range(2, limit):
        if number % i == 0:
            factors.append((i, number // i))
    return factors


if __name__ == "__main__":
    '''Reads the input file.'''
    if len(sys.argv) != 2:
        raise ValueError("Usage: factors <file>")

    input_file = sys.argv[1]

    try:
        with open(input_file, 'r') as f:
            numbers = f.readlines()
    except FileNotFoundError:
        raise FileNotFoundError("File not found")

    start_time = time.time()

    '''Loops over each line (which should contain one natural number per line),
    and calls factorize on each number.
    If factorize returns a list of factors,
    it prints the factorization in the desired format.
    '''
    for line in numbers:
        number = int(line.strip())
        factors = factorize(number)
        if factors:
            for factor in factors:
                p, q = factor
                print(f"{number}={p}*{q}")

        '''If the elapsed time exceeds 5 seconds,
        the program exits with an error message.
        '''
        if time.time() - start_time > 5:
            raise RuntimeError("Time limit exceeded")

