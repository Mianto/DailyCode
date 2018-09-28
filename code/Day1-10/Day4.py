"""
Given an array of integers, find the first missing positive integer in linear time and constant space. 
In other words, find the lowest positive integer that does not exist in the array. 
The array can contain duplicates and negative numbers as well.

Input : [3, 4, -1, 1] 
Output : 2
Input: [1, 2, 0] 
Output: 3
"""

def solve(arr):
    n = len(arr)
    i = 0
    while i < n:
        curr = arr[i]
        if curr <= 0:
            i += 1
        elif curr > 0 and curr <= n and arr[curr - 1] == curr:
            i += 1
        else:
            arr[curr - 1], arr[i] = arr[i], arr[curr - 1]

    for i in range(n):
        if arr[i] != i + 1:
            return i + 1

    return n + 1

def main():
    arr = list(map(int, input().rstrip().split()))
    print(solve(arr))


if __name__ == '__main__':
    main()