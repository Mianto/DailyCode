# -*- coding: utf-8 -*-
"""
Given an integer k and a string s, find the length of the longest
substring that contains at most k distinct characters.

For example, given s = "abcba" and k = 2, the longest substring with
k distinct characters is "bcb".

"""
MAX_CHARS = 26

def is_valid(count, k):
    n = 0
    for c in count:
        if c > 0:
            n += 1
    return k >= n

def longest_substring(s, k):
    n = len(s)
    unique = 0
    count = [0 for _ in range(MAX_CHARS)]

    for i in range(n):
        if count[ord(s[i])-ord('a')] == 0:
            unique += 1
        count[ord(s[i])-ord('a')] += 1

    if k > unique:
        print("Not enough unique characters")
        return

    curr_start, curr_end = 0, 0
    max_start, max_size = 0, 1
    count = [0 for _ in range(MAX_CHARS)]
    count[ord(s[0]) - ord('a')] += 1
    for i in range(1, n):
        count[ord(s[i]) - ord('a')] += 1
        curr_end += 1

        while not is_valid(count, k):
            count[ord(s[curr_start]) - ord('a')] -= 1
            curr_start += 1

        if curr_end - curr_start + 1 > max_size:
            max_size = curr_end - curr_start + 1
            max_start = curr_start

    return s[max_start: max_size]


def main():
    string = input()
    k = int(input())
    print(longest_substring(string, k))


if __name__ == "__main__":
    main()
