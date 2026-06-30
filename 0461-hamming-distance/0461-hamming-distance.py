class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        result = x ^ y
        distance = 0
        
        while result > 0:
            result &= (result - 1)  
            distance += 1
        return distance