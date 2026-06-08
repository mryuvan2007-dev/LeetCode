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
        
        nums = [] #create a list to store values from linked list 

    # Store values in a list
        temp = head 
        while temp: # loop it
            nums.append(temp.val) #add values in the list
            temp = temp.next #loop it manually like i=i+1

    # Sort the list
        nums.sort() # sort using inbulit function

    # Put sorted values back
        temp = head
        i = 0
        while temp:
            temp.val = nums[i] # rewrite into tthe list
            i += 1
            temp = temp.next

        return head 