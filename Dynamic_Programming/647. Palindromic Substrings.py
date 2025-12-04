class Solution:
    def countSubstrings(self, s: str) -> int:

        """
        check internal string is valid than expand the sub string till it is  palindrome
        like 
          abbd
              a --  ??b-b?? -- a       
        
        """
        def solve(l,r):
            cnt = 0

            while l>=0 and r<n and s[l] == s[r]:
                cnt+=1
                l-=1
                r+=1
            
            return cnt


        n = len(s)
        res = 0
        for i in range(n):
            res+=solve(i, i)  # odd length palindrome
            res+=solve(i, i+1) # even length palindrome

        return res


# recursive approach with meorization
class Solution:
    def countSubstrings(self, s: str) -> int:

        """
        check internal string is valid than expand the sub string till it is  palindrome
        
        """
        def solve(i, j):
            if i >= j:
                return 0

            if (i, j) in dp:
                dp[(i,j)]
            cnt = 0
            cnt+=solve(i+1, j)
            cnt+=solve(i, j-1)
            cnt -= solve(i+1, j-1)

            if s[i:j+1] == s[i:j+1][::-1]:
                cnt += 1

            dp[(i,j)] = cnt
            return dp[(i,j)]

        n = len(s)
        dp = {}
        return n+solve(0, n-1)
         
        
    # using dp tabulation

# tabulation
"""
Approach

all single char will be a palindrome

now all adjacent char which are same will be a plindrome

now if a i and j char is equal then check if i+1, j-1 is 1 (palindrome)
True: then cnt++ and dp[i][j] = dp[i-1][j-1]
False: No Change


"""
def countSubstrings(self, s: str) -> int:
  n=len(s)
  cnt = n

  dp = [[0]*(n+1) for i in range(n+1)]

  for i in range(1, n+1):
      dp[i][i] = 1

  # check ajacent values is eauql
  for i in range(1, n):
      if s[i-1] == s[i]:
          dp[i][i+1] = 1
          cnt += 1
  
  for i in range(n-2, 0, -1):
      for j in range(i+2, n+1):
          # if equal
          if s[i-1] == s[j-1] and dp[i+1][j-1]:
              dp[i][j] = 1
              cnt += 1

          
  return cnt
    
