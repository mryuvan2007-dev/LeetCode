# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        result=[]
        def dfs(node): #depth first search method
            if not node:# base case
             return []
            dfs(node.left)        # Left
            result.append(node.val)  # Root
            dfs(node.right)       # Right
        
        dfs(root) # call as recursively
        return result