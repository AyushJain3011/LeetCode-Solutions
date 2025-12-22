class Solution:
    def minInsertions(self, s: str) -> int:
        # def solve(i, j):
        #     if i == n or j == n:
        #         return 0

        #     if dp[i][j] != -1: return dp[i][j]
        #     ans = 0
        #     if s[i] == s2[j]:
        #         ans = 1 + solve(i+1, j+1)
        #     else:
        #         ans = max(solve(i+1, j), solve(i, j+1))

        #     dp[i][j] = ans
        #     return dp[i][j]

        n = len(s)
        s2 = s[::-1]
        dp=[[0]*(n+1) for _ in range(n+1)]

        for i in range(n-1, -1, -1):
            for j in range(n-1, -1, -1):
                if s[i] == s2[j]:
                    dp[i][j] = dp[i+1][j+1] + 1
                else:
                    dp[i][j] = max(dp[i+1][j],dp[i][j+1])

        return n - dp[0][0]


        



        