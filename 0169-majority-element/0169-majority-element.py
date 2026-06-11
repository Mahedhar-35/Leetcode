class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s=list(set(nums))
        for i in s:
            count=0
            for j in nums:
                if i==j:
                    count+=1
            if count>len(nums)/2 :
                return i       