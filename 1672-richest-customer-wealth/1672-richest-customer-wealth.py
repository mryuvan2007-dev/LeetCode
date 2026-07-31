class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        sums=0
        
        for i in accounts:
            curr=sum(i)
            if(curr>sums):
                sums=curr
        return sums
        