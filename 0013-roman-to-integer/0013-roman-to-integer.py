class Solution(object):
    def romanToInt(self, s):
        sum=0
        values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        prev=0
        for i in range(len(s)):
            curr=values[s[i]]
            if curr>prev:
                sum-=2*prev
            sum+=curr
            prev=curr
        return sum
