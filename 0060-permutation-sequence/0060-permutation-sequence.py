class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        numbers = []
        for i in range(1, n + 1):
            numbers.append(str(i))
        k = k - 1
        
        factorials = [1] * n
        for i in range(1, n):
            factorials[i] = factorials[i - 1] * i
            
        result = []
        for i in range(n - 1, -1, -1):
            block_size = factorials[i]
            
            index = k // block_size
            
            chosen_digit = numbers[index]
            result.append(chosen_digit)
            numbers.pop(index)
            
            k = k % block_size
            
        return "".join(result)