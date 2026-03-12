class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        words = s.split()      # Split the string into words
        last_word = words[-1]  # Get the last word using index value -1
        length = len(last_word) # len () find the length of the last word
        return length
        