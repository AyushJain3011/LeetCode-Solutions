class Solution:
    
    """
    we are using just opposite approach

    we are decresing the other numbers so that they become equal 
    and for this we have to decrement each number and that difference give the moves count
    
    """
    def minMoves(self, nums: List[int]) -> int:
        if len(set(nums)) == 1:
            return 0

        mini = min(nums)
        cnt = 0
        for num in nums:
            cnt += num - mini
        
        return cnt
    


    """
    at the end of  (m) moves the smallest element became = mini + m
    what will be increment after m moves
      each moes we increse n-1 elements by 1
      then after m moves---> m*(n-1)

      so 
      total_sum = initial_sum + increment
      n*(mini + m) = S + m(n-1)
      .
      .
      after solving
      .
      .
      m = S - n*(mini)

    """