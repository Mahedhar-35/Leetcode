# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        countp = []
        countq = []
        
        def preorder(root, count):
            if root is None:
                count.append(None)
                return 
            count.append(root.val)
            preorder(root.left, count)
            preorder(root.right, count)
            
        preorder(p, countp)
        preorder(q, countq)
        
        if countp == countq:
            return True 
        else:
            return False