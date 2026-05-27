class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        result = []
        
        def backtrack(start, current_combination):
            if len(current_combination) == k:
                result.append(list(current_combination))
                return
            
            for num in range(start, n + 1):
                current_combination.append(num)
                backtrack(num + 1, current_combination)
                current_combination.pop()
        backtrack(1, [])
        return result