class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        def factorial(n):
            if n==1: return 1
            return n*factorial(n-1)


        def solve(k, N):
            if N == 1:
                for num in range(1, n+1):
                    if num not in visited:
                        return str(num)
                 

            
            fact = factorial(N) // N
            string = ""
            for num in range(1, n+1):
                
                # if k is greater
                if num in visited:
                    continue
                elif k > fact:
                    k-=fact
                else:
                    string += str(num)
                    visited.add(num)
                    string += solve(k, N-1)
                    break
            
            return string

        visited = set()
        return solve(k, n)



            
        

        