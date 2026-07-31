class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # we are start adding from the previous value so start from 1 index
        for i in range(1,len(nums)):
            # add the element from the previous element
            nums[i]+=nums[i-1]
        return nums
        