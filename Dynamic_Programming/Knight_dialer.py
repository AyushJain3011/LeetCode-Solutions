class Solution:
    def knightDialer(self, n: int) -> int:
        """
        now the dp holds the count of the phone number which are going to end with the index value
        Like: dp[8-1] = 2
        means there are two type of number which are going to end with 8
        at end we are going to sum all the value in the dp
        
        """

        if n == 1:
            return 10

        mod = 10**9+7
        moves = [[4,6],[6,8],[7,9],[4,8],[9,3,0],[],[7,1,0],[2,6],[1,3],[2,4]]
        ans = 0
        dp = [1]*10

        for i in range(n-1):
            new_dp = [0]*10
            for i in range(10):
                for nxt in moves[i]:
                    new_dp[nxt] = (new_dp[nxt] + dp[i])%mod
                
            dp=new_dp


        return sum(dp)%mod

