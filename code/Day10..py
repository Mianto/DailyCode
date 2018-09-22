# -*- coding: utf-8 -*-
"""
Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.
"""
from functools import wraps, partial
from time import sleep

"""
def outside_wrapper(_func, sleep_time):
    @wraps(_func)
    def wrapper(*args, **kwargs):
        sleep(sleep_time)
        return _func(*args, **kwargs)
    return wrapper

n = int(input())
job_schedule = partial(outside_wrapper, sleep_time = n)

@job_schedule
def add(a, b):
    return (a + b)
"""

def job_schedule(sleep_time):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            sleep(sleep_time)
            return func(*args, **kwargs)
        return wrapper
    return decorator

def schedule(n, func, *args, **kwargs):
    return job_schedule(n/1000)(func)(*args, **kwargs)

def add(a, b):
    return a + b


def main():
    n = int(input())
    print(schedule(n, add, 4, 7))


if __name__ == '__main__':
    main()




