class Solution(object):
    def generate(self, n):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result = []
        
        for i in range(n):
            row = [1] * (i + 1)  # create row with all 1s
            
            # fill middle values
            for j in range(1, i):
                row[j] = result[i-1][j-1] + result[i-1][j]
            
            result.append(row)
        
        return result