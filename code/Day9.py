# -*-coding: utf-8 -*-
"""
Given a list of integers, write a function that returns the largest sum of non-adjacent numbers.
Numbers can be zero or negative.

Input: [2, 4, 6, 2, 5]
Output: 13
Since we pick 2, 6, 5
Input: [5, 1, 1, 5]
Output: 10
Since we pick 5 and 5

Follow-up: Can you do this in O(n) time and constant space.
"""

def main():
    arr = list(map(int, input().strip().split()))
    n = len(arr)
    incl = 0
    exclud = 0
    for i in range(n):
        exclud_new = exclud if exclud > incl else incl
        incl = arr[i] + exclud
        exclud = exclud_new

    print(incl)

if __name__ == '__main__':
    main()