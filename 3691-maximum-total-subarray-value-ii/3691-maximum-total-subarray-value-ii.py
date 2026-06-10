import heapq
class Solution(object):
    def maxTotalValue(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        heap = []
        
        K = 17 
        st_max = [[0] * K for _ in range(n)]
        st_min = [[0] * K for _ in range(n)]
        
        for i in range(n):
            st_max[i][0] = nums[i]
            st_min[i][0] = nums[i]
            
        for j in range(1, K):
            for i in range(n - (1 << j) + 1):
                st_max[i][j] = max(st_max[i][j-1], st_max[i + (1 << (j-1))][j-1])
                st_min[i][j] = min(st_min[i][j-1], st_min[i + (1 << (j-1))][j-1])
                
        def query_val(L, R):
            length = R - L + 1
            j = length.bit_length() - 1
            mx = max(st_max[L][j], st_max[R - (1 << j) + 1][j])
            mn = min(st_min[L][j], st_min[R - (1 << j) + 1][j])
            return mx - mn

        visited = set()
        
        val = query_val(0, n - 1)
        heapq.heappush(heap, (-val, 0, n - 1))
        visited.add((0, n - 1))
        
        total_value = 0
        count = 0
        
        while heap and count < k:
            neg_val, L, R = heapq.heappop(heap)
            val = -neg_val
            
            total_value += val
            count += 1
            if L < R:
                if (L + 1, R) not in visited:
                    visited.add((L + 1, R))
                    heapq.heappush(heap, (-query_val(L + 1, R), L + 1, R))
                if (L, R - 1) not in visited:
                    visited.add((L, R - 1))
                    heapq.heappush(heap, (-query_val(L, R - 1), L, R - 1))
                    
        return total_value