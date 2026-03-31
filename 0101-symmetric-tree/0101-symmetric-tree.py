# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isTreeSymmetric(self, leftRoot, rightRoot):
        #return true when both the nodes are empty
        if leftRoot is None and rightRoot is None:
            return True
        #return false when any one of the node is empty
        if (leftRoot is None and rightRoot is not None) or (leftRoot is not None and rightRoot is None):
            return False
        #return false when the values of the nodes are not equal
        if leftRoot.val != rightRoot.val:
            return False
        # makes it as recursive
        return self.isTreeSymmetric(leftRoot.left, rightRoot.right) and self.isTreeSymmetric(leftRoot.right, rightRoot.left)
    #creating a function to check the tree values are symmetric
    def isSymmetric(self, root):
        return self.isTreeSymmetric(root.left, root.right)
        