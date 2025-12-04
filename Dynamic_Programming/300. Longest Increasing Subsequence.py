class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
  
        # def solve(ind, prev_ind):
        #     nonlocal max_len
        #     if ind < 0:
        #         return 0

        #     if dp[ind][prev_ind] != -1:
        #         return dp[ind][prev_ind]

        #     # take
        #     t, nt = 0, 0
        #     if prev_ind == -1 or nums[ind] < nums[prev_ind]:
        #         t = 1 + solve(ind-1, ind)
             
        #      # not Take
        #     nt = solve(ind-1, prev_ind)

        #     dp[ind][prev_ind] = max(t, nt)
        #     # max_len = max(max_len, dp[(ind, val)])

        #     return dp[ind][prev_ind]

        # n = len(nums)
      
        # dp = [[-1]*(n+1) for _ in range(n)]
        # return solve(n-1, -1)
        

"""
Approach-2

we start taking number from the strcktly incresing order

if next ind value is less then we fingure out the right position of replace that value
        0 1 2 3 4 5
nums = [0,1,0,3,2,3]
res = 
ind 0 - res = [0]
ind 1 - res = [0,1]
ind 2 - now ind value is not greater than the last ind value of res then we have to fingure out he right index to replace that value
    res - [0,1]
ind 3 - res = [0,1,3]
ind 4 - replace the 2 with right place 
    res - [0,1,2]
ind 5 - res = [0,1,2,3]

"""
# let's start implementation

n = len(nums)
res = [nums[0]]

for i in range(1, n):
    
    if res[-1] < nums[i]:
        res.append(nums[i])

    else:
        ind = 0

        while ind < len(res):
            if nums[ind] < nums[i]:
                ind+=1
        
        res[ind] = nums[i]


return len(res)

    


        



           