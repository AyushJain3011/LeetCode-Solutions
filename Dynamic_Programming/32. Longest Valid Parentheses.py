
"""
()(() ---> 2
(()))) ---> 4
))()() --->2
))(()) ---> 2

if need to make sure those opening parentheis must be pop up if they are not popped up then they are not part of combinatio

also if there is closing parenthesis and stack have not open parenthesis then they are no part of longest valid parenthesis
"""

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        """
        Time Comp : O(n)
        Space Comp: O(n)
        Auxilary Space: O(n)
        """

        def leng_valid_para(i):
            
            if i == n:
                return 0

            leng = 0
            if s[i] == ')':
                if st and s[st[-1]]=='(':
                    st.pop()
                    leng = 2 + leng_valid_para(i+1)
                else:
                    val = leng_valid_para(i+1)
            else:
                st.append(i)
                leng = leng_valid_para(i+1)
                # if that ith index is exist in the stack then those previous count of parenthesis willnot be count
                if st and st[-1]==i:
                    st.pop()
                    leng=0

            self.max_leng = max(self.max_leng, leng)
            return leng

        n=len(s)
        st = []
        self.max_leng = 0
        l = leng_valid_para(0)

        return self.max_leng




# Removing auxilary space
"""
st = [-1]
if there is "(" then add that index in stack

if closing bracket then pop the top most index
  if st empty add the current index
  else:
    
(())((
-1,0
res = 2-1+1 = 2
res = 3 - 0 + 1



"""

def solve(s):
    n = len(s)
    st = []
    res = 0
    for i in range(n):
        if s[i] == '(':
          st.append(i)
        else:
            st.pop()
            if not st:
              st.append(i)
            else:
              res = max(res, i - st[-1] + 1)
      
    return res
            
        


        






















