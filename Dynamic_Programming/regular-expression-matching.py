class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        

        def check(i, j):
            if (i, j) in dp:
                return dp[(i, j)]

            if j == len(p):
                return i == len(s)

            # if char are same or p[j] == "."
            match = i < len(s) and (s[i] == p[j] or p[j] == ".")

            if j+1 < len(p) and p[j+1] == '*':
                # either skil x* or take this
                ans =  check(i, j+2) or (match and check(i+1, j))
            else:
                ans = match and check(i+1, j+1)

            dp[(i, j)] = ans
            return dp[(i, j)]

        n, m = len(s), len(p)
        # dp = {}
        # return check(0, 0)  





        # /////////////////// Tabulation ////////////////////
        dp = [[False]*(m+1) for _ in range(n+1)]
        dp[0][0] = True

        for i in range(1, m+1):
            dp[0][i] = i > 1 and p[i-1] == "*" and dp[0][i-2]
               
            

        for i in range(1, n+1):
            for j in range(1, m+1):

                if p[j-1] == '*':
                    dp[i][j] = dp[i][j-2] or ((s[i-1] == p[j-2] or p[j-2] == '.') and dp[i-1][j])
                else:
                    dp[i][j] = (s[i-1] == p[j-1] or p[j-1] == '.') and dp[i-1][j-1]

        
        return dp[n][m]


        
        

