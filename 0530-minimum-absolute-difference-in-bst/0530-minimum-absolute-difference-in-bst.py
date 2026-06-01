# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getMinimumDifference(self, root):
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
        m=10**6 
        for i in range(1,len(count)):
            if (count[i]-count[i-1])<m:
                m=count[i]-count[i-1]
        return m             