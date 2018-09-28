# -*- coding: utf-8 -*-
"""
The area of a circle is defined as πr^2. Estimate π to 3 decimal places
using a Monte Carlo method.

Hint: The basic equation of a circle is x^2 + y^2 = r^2.
"""

import random

def main():
    circle_point, square_point = 0, 0
    for i in range(1000000):
        x = random.random()
        y = random.random()

        if (x * x + y * y) <= 1:
            circle_point +=  1

        square_point += 1

        pi = 4 * circle_point / square_point
    print(pi)



if __name__ == "__main__":
    main()
