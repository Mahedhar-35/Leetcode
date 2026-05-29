# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        count=[]
        def Traversal(root):

            if root==None:
                return 
            Traversal(root.left)
            count.append(root.val)
            Traversal(root.right)
        Traversal(root)    
        return count    