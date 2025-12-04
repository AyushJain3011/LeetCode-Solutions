class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        def solve(string):
            if not string:
                return [""]

            if string in dp:
                return dp[string]

            segments = []
            for word in wordDict:

                if string.startswith(word):
                    for s in solve(string[len(word):]):
                        temp = word
                        if s != "":
                            temp += " " + s
                        segments.append(temp)
                        
            dp[string] = segments
            return dp[string]
                


        dp = {}
        return solve(s)