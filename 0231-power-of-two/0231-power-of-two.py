class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        i=0
        if n<0:
            return False
        while pow(2,i)<=n:
            if pow(2,i)==n:
                return True
            i+=1
        return False
        