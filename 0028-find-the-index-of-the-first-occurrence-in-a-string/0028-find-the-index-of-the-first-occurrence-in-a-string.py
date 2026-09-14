class Solution(object):
    def strStr(self, big, small):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        for i in range(len(big) - len(small) + 1):
            if big[i:i + len(small)] == small:
                return i

        return -1