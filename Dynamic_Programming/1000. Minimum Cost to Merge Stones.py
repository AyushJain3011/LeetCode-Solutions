class Solution:
    def mergeStones(self, stones: List[int], K: int) -> int:
        """
        
        """

        n = len(stones)

        # If it's impossible to end with 1 pile
        if (n - 1) % (K - 1) != 0:
            return -1

        # prefix sum (auxiliary space)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i+1] = prefix[i] + stones[i]

        def range_sum(i, j):
            return prefix[j+1] - prefix[i]

        # dp[i][j][p] = minimum cost to merge stones[i..j] into p piles
        dp = [[[-1 for _ in range(K + 1)] for _ in range(n)] for _ in range(n)]

        def solve(i, j, p):
            # Base: single pile
            if i == j:
                return 0 if p == 1 else float('inf')

            # memo check
            if dp[i][j][p] != -1:
                return dp[i][j][p]

            # Case 1: want 1 pile -> must first form K piles
            if p == 1:
                cost = solve(i, j, K) + range_sum(i, j)
                dp[i][j][p] = cost
                return cost

            # Case 2: want p piles (2 <= p <= K)
            ans = float('inf')

            # Only split at steps of K-1 to allow legal merges
            for mid in range(i, j, K - 1):
                # left must become exactly 1 pile
                left = solve(i, mid, 1)
                # right must become p-1 piles
                right = solve(mid + 1, j, p - 1)
                ans = min(ans, left + right)

            dp[i][j][p] = ans
            return ans

        return solve(0, n - 1, 1)A
