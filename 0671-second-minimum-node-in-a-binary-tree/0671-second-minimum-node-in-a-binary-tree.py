# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        count=[]
        def trav(root):
            if root is None:
                return
            count.append(root.val)
            trav(root.left)
            trav(root.right)
        trav(root)
        count=sorted(count)
        min2=count[0]    
        for i in count:
            if i>min2:
                return i
        return -1        
