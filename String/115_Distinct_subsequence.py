class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        n, m = len(s), len(t)
        dp = [[0]*(m+1) for _ in range(n+1)]

        # An empty string can be form by skipping all the character of string(s) that why we are placing one in the first row of dp
        for i in range(n+1):
            dp[i][0] = 1

        for j in range(1, m+1):
            for i in range(1, n+1):

                dp[i][j] = dp[i-1][j]
                if s[i-1] == t[j-1]:
                    dp[i][j] += dp[i-1][j-1]

        return dp[n][m]



    # recursive Approach
    def find_sequence(self, i, j, s, t, dp):
        if j == len(t):
            return 1
        
        if i == len(s):
            return 0

        if dp[i][j] != -1:
            return dp[i][j]

        # if index value same then take it
        cnt = 0
        if s[i] == t[j]:
            cnt = self.find_sequence(i+1, j+1, s, t, dp)
        
        cnt += self.find_sequence(i+1, j, s, t, dp)
        
        dp[i][j] = cnt
        return dp[i][j]



        

        