class Solution:
    def minDifficulty(self, jd: List[int], d: int) -> int:
        
        def solve(ind, rem_d):
            if ind == n and rem_d==0:
                return 0
            elif ind == n or rem_d==0:
                return 1001

            if (ind, rem_d) in dp:
                return dp[(ind, rem_d)]

            min_diff = float('inf')
            maxi = 0

            for i in range(ind, n-rem_d+1):
                maxi = max(maxi, jd[i])
                min_diff = min(min_diff, maxi + solve(i+1, rem_d - 1))

            dp[(ind, rem_d)] =min_diff
            return dp[(ind, rem_d)]


         n = len(jd)

        if d > n:
            return -1
        elif d==n: return sum(jd)
        # dp = {}
        # return solve(0, d)
       
        
# /////////////////   Tabulation ////////////////////
        dp = [[float('inf')]*d for _ in range(n)]

        # if day is one
        max_diff = 0
        for i in range(n):
            max_diff = max(max_diff, jd[i])
            dp[i][0] = max_diff

        # start for 2nd day
        for j in range(1, d):
            for i in range(j, n):

                max_diff = 0

                # taking each value to calcualate minimum
                for k in range(i, j-1, -1):
                    max_diff = max(max_diff, jd[k])
                    dp[i][j] = min(dp[i][j], dp[k-1][j-1]+max_diff)
        
 

        return dp[n-1][d-1]

        
        