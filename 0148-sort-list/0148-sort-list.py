# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        nums = []

    # Store values in a list
        temp = head
        while temp:
            nums.append(temp.val)
            temp = temp.next

    # Sort the list
        nums.sort()

    # Put sorted values back
        temp = head
        i = 0
        while temp:
            temp.val = nums[i]
            i += 1
            temp = temp.next

        return head