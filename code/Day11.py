# -*- coding: utf-8 -*-
"""

Implement an autocomplete system. That is given a query string s and a
set of all possible query strings, return all strings in the set that
have s as an prefix

"""
# can be solve using Trie

def main():
    s = 'de'
    li = ['dog', 'deer', 'deal']
    for x in li:
        if s in x:
            print(x)



if __name__ == "__main__":
    main()
