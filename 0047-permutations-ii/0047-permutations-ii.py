class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        nums.sort()
        visited = [False] * len(nums)
        
        def backtrack(cp):
            if len(cp) == len(nums):
                result.append(list(cp))
                return
                
            for i in range(len(nums)):
                if visited[i]:
                    continue
                if i > 0 and nums[i] == nums[i - 1] and not visited[i - 1]:
                    continue
                visited[i] = True
                cp.append(nums[i])
                backtrack(cp)
                cp.pop()
                visited[i] = False
                
        backtrack([])
        return result