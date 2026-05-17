class Solution(object):
    def smallestUniqueSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sml = nums
        n = len(sml)
        
        MOD1 = 1000000007
        MOD2 = 1000000009
        BASE1 = 313
        BASE2 = 317
        
        def has_unique_subarray(length):
            hash_counts = {}
            pow1 = pow(BASE1, length, MOD1)
            pow2 = pow(BASE2, length, MOD2)
            
            h1 = 0
            h2 = 0
            for i in range(length):
                h1 = (h1 * BASE1 + sml[i]) % MOD1
                h2 = (h2 * BASE2 + sml[i]) % MOD2
                
            hash_counts[(h1, h2)] = 1
            
            for i in range(length, n):
                h1 = (h1 * BASE1 + sml[i] - sml[i - length] * pow1) % MOD1
                h2 = (h2 * BASE2 + sml[i] - sml[i - length] * pow2) % MOD2
                if h1 < 0: h1 = (h1 % MOD1 + MOD1) % MOD1
                if h2 < 0: h2 = (h2 % MOD2 + MOD2) % MOD2
                
                pair = (h1, h2)
                hash_counts[pair] = hash_counts.get(pair, 0) + 1
            for count in hash_counts.values():
                if count == 1:
                    return True
            return False
        low = 1
        high = n
        ans = n
        
        while low <= high:
            mid = (low + high) // 2
            if has_unique_subarray(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
                
        return ans