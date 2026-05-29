# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[Optional[TreeNode]]
        """
        if n == 0:
            return []
            
        def trees(start, end):
            if start > end:
                return [None]
                
            all_trees = []
            
            for i in range(start, end + 1):
                
                leftsub = trees(start, i - 1)
                rightsub = trees(i + 1, end)
                
                for left in leftsub:
                    for right in rightsub:
                        root = TreeNode(i)
                        root.left = left
                        root.right = right
                        all_trees.append(root)
                        
            return all_trees

        return trees(1, n)