# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.result = 0
        
        def traverse(root):
            if root is None:
                return
            if root.left and root.left.left is None and root.left.right is None:
                self.result += root.left.val
            traverse(root.left)
            traverse(root.right)
        traverse(root)
        return self.result 