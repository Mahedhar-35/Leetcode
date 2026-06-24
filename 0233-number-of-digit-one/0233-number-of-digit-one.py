class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return 0
            
        count = 0
        i = 1  
        
        while i <= n:
            divider = i * 10
            left = n // divider
            curr = (n // i) % 10
            right = n % i
            
            if curr == 0:
                count += left * i
            elif curr == 1:
                count += (left * i) + right + 1
            else:
                count += (left + 1) * i
                
            i *= 10
            
        return count