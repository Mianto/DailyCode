"""
Given an array of integers, return a new array such that each element at index i of the new array 
is the product of all the numbers in the original array except the one at i.

Input 1: [1, 2, 3, 4, 5], 
Output 1: [120, 60, 40, 30, 24]
Input 2: [3, 2, 1] 
Output 2: [2, 3, 6]
"""

def solve(arr):
    mul = 1
    li = list()
    for i in range(len(arr)):
        li.append(0)
        mul *= arr[i]
    
    for i in range(len(arr)):
        li[i] = mul // arr[i]
    
    return li


def print_list(arr):
    for x in arr:
        print(x, end=" ")
    print()


def main():
    arr = list(map(int, input().rstrip().split()))
    print_list(solve(arr))


if __name__ == '__main__':
    main()
