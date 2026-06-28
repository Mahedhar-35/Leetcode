class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        c=0
        i=1
        while n>0 and n>=i:
            c+=1
            n-=i
            i+=1
        return c    