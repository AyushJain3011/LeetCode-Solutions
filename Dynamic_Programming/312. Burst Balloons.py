class Solution:
    def maxCoins(self, nums: List[int]) -> int:

        """
        either selecting the balloon, we will burst the seleced balloon in the end because that is not dependent on any other ballon
        Like:
        nums = 3, 1, 5, 8
        We can select 0, 1, 2 ,3
        suppose we are at 2nd index
                5 --> Before calculating we burst all the left and right ballon 
        [3, 1, 5]      [5, 8]
        
        
        
        """
        def solve(l, r):
            if l + 1 == r:
                return 0

            if dp[l][r] != -1:
                return dp[l][r]
            
            max_b = 0
            for i in range(l+1, r):
                curr = solve(l, i) + solve(i, r) + balloons[l]*balloons[i]*balloons[r]
                max_b = max(curr, max_b)

            dp[l][r] = max_b

            return dp[l][r]



        balloons = [1] + nums + [1]
        n = len(balloons)
        dp = [[-1]*n for _ in range(n)]
        return solve(0, n-1)



        
        