'''
Given an array of integers, return a new array such that each element at index i of the new array
is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24].
If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?
'''
import numpy as np

def d2(inp):
    p = 1
    a = [0]*(len(inp))
    for i in range(len(inp)):
        a[i] = p
        p = p * inp[i]
    p = 1
    b = [0]*(len(inp))
    #print(b)
    for y in range(len(inp)):
        i = len(inp)-y-1
        #print(i)
        b[i] = p
        p = p * inp[i]
    out = [0]*(len(inp))
    for i in range(len(inp)):
        out[i] = a[i]*b[i]
    return out

def d2a(inp):
    p1 = 1
    p2 = 1
    a = [0]*(len(inp))
    b = [0]*(len(inp))
    for i in range(len(inp)):
        a[i]=p1
        p1 = p1 * inp[i]
        y = len(inp)-i-1
        b[y]=p2
        p2 = p2 * inp[y]
    out = [0]*(len(inp))
    for i in range(len(inp)):
        out[i] = a[i]*b[i]
    return out


inp = [3,2,1]
print(d2(inp))
