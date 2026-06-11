class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        t=n
        while t>=1:
            if t==1:
                return True
            if t%2==1:
                return False    
            t=float(t/2)
        return False        