'''
Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.

For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".
'''

def d13(input,k):
    temp = ''
    i = 0
    arr = []
    for char in input:
        if(temp!=char):
            i+=1
        arr.append(i)
        temp = char
    return arr


s = "abcba"
k = 2
print(d13(s,k))
