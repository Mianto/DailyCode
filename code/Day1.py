__author__ = 'Siddhant'

'''
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
'''

def solve_naive(a, k):
    n = len(a)
    for i in range(n):
        for j in range(i, n):
            if a[i] + a[j] == k:
                return 1
    return 0


def solve_sort(a, k):
    left = 0
    right = len(a) - 1

    a.sort()
    while left < right:
        if a[left] + a[right] == k:
            return 1
        elif a[left] + a[right] > k:
            right -= 1
        else:
            left += 1
    return 0


def solve_hash(arr, k):
    di = dict()

    for i in range(len(arr)):
        if k - arr[i] in di.keys():
            return 1
        di[arr[i]] = 1
    return 0


def main():
    arr = list(map(int, input().rstrip().split()))
    k = int(input())
    # print(solve_naive(arr, k))
    # print(solve_sort(arr, k))
    print(solve_hash(arr, k))


if __name__ == '__main__':
    main()