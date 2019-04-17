'''
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
'''

def d1(inp,k):
    for i in range(len(inp)):
        t1 = k-inp[i]
        if t1 in inp:
            return True
    return False

print(d1([10,15,3,7],17))
