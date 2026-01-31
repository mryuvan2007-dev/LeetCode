class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        result=0
        
        for i in digits:
            result = result * 10 + i
        result+=1
        return list(map(int, str(result)))

