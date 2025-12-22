class Solution:
    def minMoves(self, a: List[int]) -> int:
        n = len(a)
        s = sum(a)
        if s < 0: 
            return -1
        # mext function take iterable and default value
        j = next((i for i,v in enumerate(a) if v < 0), -1)
        if j == -1: 
            return 0
        d = -a[j]
        b = []
        for i,v in enumerate(a):
            if v > 0:
                dist = min((i-j)%n, (j-i)%n)
                b.append((dist, v))
        b.sort()
        m = 0
        for dist,v in b:
            t = min(v, d)
            m += t * dist
            d -= t
            if d == 0: 
                return m
        return -1