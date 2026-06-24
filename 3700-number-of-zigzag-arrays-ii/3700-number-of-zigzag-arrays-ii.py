class Solution(object):
    def zigZagArrays(self, n, l, r):
        """
        :type n: int
        :type l: int
        :type r: int
        :rtype: int
        """
        MOD = 10**9 + 7
        K = r - l + 1
        
        if K <= 1 or n < 3:
            return 0
            
        SIZE = 2 * K
        
        def multiply(A, B):
            C = [[0] * SIZE for _ in range(SIZE)]
            for i in range(SIZE):
                for k in range(SIZE):
                    if A[i][k] == 0:
                        continue
                    for j in range(SIZE):
                        C[i][j] = (C[i][j] + A[i][k] * B[k][j]) % MOD
            return C

        def power(matrix, p):
            result = [[0] * SIZE for _ in range(SIZE)]
            for i in range(SIZE):
                result[i][i] = 1  
                
            base = matrix
            while p > 0:
                if p % 2 == 1:
                    result = multiply(result, base)
                base = multiply(base, base)
                p //= 2
            return result

        X2 = [0] * SIZE
        for v in range(K):
            X2[v] = v
            X2[K + v] = K - 1 - v

        M = [[0] * SIZE for _ in range(SIZE)]
        for v in range(K):
            for prev in range(v):
                M[v][K + prev] = 1
            for prev in range(v + 1, K):
                M[K + v][prev] = 1

        M_pow = power(M, n - 2)

        total_arrays = 0
        for i in range(SIZE):
            row_sum = 0
            for j in range(SIZE):
                row_sum = (row_sum + M_pow[i][j] * X2[j]) % MOD
            total_arrays = (total_arrays + row_sum) % MOD

        return total_arrays