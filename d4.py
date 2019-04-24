'''
Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.
'''

def d6(inp):
    high = max(inp)
    if(len(inp)>=high):
        high = len(inp)
    x = [0 for i in range(high)]
    print(x)

    for i in range(high):
        x[inp[i]-1]=1

    for i in range(high):
        if(x[i]==0):
            return i+1

    print(x)
    return high

print(d6( [1, 2, 0, 3, 5] ))
