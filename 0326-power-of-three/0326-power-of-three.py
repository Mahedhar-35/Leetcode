class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        t=n
        while t>=1:
            if t==1:
                return True
            if t%3!=0:
                return False    
            t=float(t/3)
        return False        