# -*- coding: utf-8 -*-
"""
There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time.
Given N, write a function that returns the number of unique ways you can climb the staircase.
The order of the steps matters.

For example, if N is 4, then there are 5 unique ways:

    1, 1, 1, 1
    2, 1, 1
    1, 2, 1
    1, 1, 2
    2, 2

What if, instead of being able to climb 1 or 2 steps at a time, you could climb any number
from a set of positive integers X?
For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.

"""
from functools import wraps

def memoize(func):
    memo = {}
    @wraps(func)
    def wrapper(*args):
        if args not in memo:
            memo[args] = func(args)
        return memo[args]
    return wrapper


@memoize
def count_step(N):
    if N <= 1:
        return 1
    return count_step(N - 1) + count_step(N - 2)

@memoize
def count_step_any(N, arr, su):
    if N <= 1:
        return 1
    for a in arr:
        su[0] += count_step_any(N - a)
    return su[0]

def main():
    N = int(input())
    print(count_step(N))


if __name__ == "__main__":
    main()