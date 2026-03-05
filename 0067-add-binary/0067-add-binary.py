class Solution(object):
    def addBinary(self, a, b):
        sum = int(a,2)+int(b,2)
        val=bin(sum)[2:]
        return val
        