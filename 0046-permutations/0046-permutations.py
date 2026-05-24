class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
                              
        def backtrack(cp):
            if len(cp) == len(nums):
                result.append(list(cp))
                return
            
            for num in nums:
                if num not in cp:
                    cp.append(num)
                    backtrack(cp)
                    cp.pop()
                    
        backtrack([])
        return result