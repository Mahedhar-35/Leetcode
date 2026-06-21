class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        digit_len = 1
        count = 9
        start = 1
        
        while n > digit_len * count:
            n -= digit_len * count
            digit_len += 1
            count *= 10
            start *= 10
            
        target_num = start + (n - 1) // digit_len 
        digit_idx = (n - 1) % digit_len
        
        return int(str(target_num)[digit_idx])