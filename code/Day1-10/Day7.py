# -*- coding: utf-8 -*-

"""
Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not allowed.
"""

def decoder(s):
    s_len = len(s)
    if s_len == 1:
        return 1
    elif s_len == 2:
        return can_decode(s) + 1
    else:
        return can_decode(s[:1]) * decoder(s[1:]) + can_decode(s[:2]) * decoder(s[2:])


def can_decode(s):
    if s == "":
        return 0
    n = int(s)
    if 1 <= n <= 26:
        return 1
    return 0


def main():
    encoded = input().rstrip()
    print(decoder(encoded))


if __name__ == '__main__':
    main()