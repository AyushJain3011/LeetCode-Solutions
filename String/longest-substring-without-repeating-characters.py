"""
# sliding window

# Take a unordered set which store the char 
take two pointer

i = 0 , j = 0
if there is any char which is repeating then move i pointer till we remove that char form the set

"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        n = len(s)
        i, j = 0, 0
        ans = 0
        d = set()

        while j < n:
            while i < j and s[j] in d:
                d.remove(s[i])
                i+=1

            ans = max(ans, j-i+1)
            d.add(s[j])
            j+=1

        return ans