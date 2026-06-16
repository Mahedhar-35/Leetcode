class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        result=[]
        for i in range(n+1):
            curr=[]
            j=i
            while j>0:
                curr.append(j%2)
                j=j//2
            result.append(sum(curr))
        return result        