class Solution(object):
    def longestCommonPrefix(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: int
        """
        prefixs = set()
        
        for num in arr1:
            s = str(num)
            for i in range(1, len(s) + 1):
                prefixs.add(s[:i])
                
        max_length = 0
        
        for num in arr2:
            s = str(num)
            if len(s) <= max_length:
                continue
                
            for i in range(1, len(s) + 1):
                prefix = s[:i]
                if prefix in prefixs:
                    max_length = max(max_length, len(prefix))
                else:
                    break
                    
        return max_length  