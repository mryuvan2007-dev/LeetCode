class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = 0
        for i in range(32):
            result = result << 1       # Shift left
            result += (n & 1)       # Add the least significant bit of n to result
            n = n >> 1           # Shift n to the right
        return result

