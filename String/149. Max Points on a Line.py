class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:

        # from collections import defaultdict
        def find_slope(c1, c2):
            return (c2[1]-c1[1])/(c2[0]-c1[0])

        ans = 1
        n = len(points)
        maxi = 1000
        for i in range(n):
            d = {}
            for j in range(i+1, n):
                if points[j][0] != points[i][0]:
                    slope = find_slope(points[i], points[j])
                else:
                    slope = maxi

                if slope not in d.keys():
                    d[slope] = 2
                else:
                    d[slope]+=1
               

                ans=max(ans, d[slope])
            # print(d)
        
        return ans
        