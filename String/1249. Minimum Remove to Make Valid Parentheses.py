"""
Docstring for String.1249. Minimum Remove to Make Valid Parentheses

Test Cases: 
1:) "lee(t(c)o)de)"
2:) "a)b(c)d"

if there is char then add that char and call the function recursively

if openinig bracket then add that in stack and call function
  when we come back check that opening parenthesis not be there if 'NO" then add that clossing parenthesis


"""
# recursive approach
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:


        def solve(ind):
            if ind == n:
                return ""
            

            if 96 < ord(s[ind]) < 123:
                return s[ind] + solve(ind+1) 
            
            string = ""
            if s[ind] == '(':
                st.append(ind)
                string = solve(ind+1)
                if st and st[-1] == ind:
                    st.pop()
                    return string
                
                string = '(' + string
                
                
            else:
                if st and s[st[-1]] == '(':
                    st.pop()
                    string = ')' + solve(ind+1)
                else:
                    string = solve(ind+1)

            return string

        n = len(s)
        st = []
        return solve(0)

# iterative approach
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        
        stack = []  # unpaired '(' indices
        chars = [c for c in s]

        for i, c in enumerate(chars):
            if c == '(':
                stack.append(i)  # Record the unpaired '(' index.
            elif c == ')':
                if stack:
                    stack.pop()  # Find a pair
                else:
                    chars[i] = '*'  # Mark the unpaired ')' as '*'.

        # Mark the unpaired '(' as '*'.
        while stack:
            chars[stack.pop()] = '*'

        return ''.join(chars).replace('*', '')

        

        