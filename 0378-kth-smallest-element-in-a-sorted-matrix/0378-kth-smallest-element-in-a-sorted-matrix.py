class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        c=[]
        for i in matrix:
            for j in i:
                c.append(j)
        c.sort()
        return c[k-1]        