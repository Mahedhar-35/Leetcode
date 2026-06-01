# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findMode(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        values=[]
        def trav(root):
            if root is None:
                return
            values.append(root.val)
            trav(root.left)
            trav(root.right)
        trav(root)
        frequencies = {}
        for num in values:
            if num in frequencies:
                frequencies[num] += 1
            else:
                frequencies[num] = 1
        max_count = 0
        for count in frequencies.values():
            if count > max_count:
                max_count = count     
        mode=[]
        for num, count in frequencies.items():
            if count == max_count:
                mode.append(num)
            
        return mode

