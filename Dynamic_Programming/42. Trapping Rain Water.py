class Solution:
    def trap(self, height: List[int]) -> int:

        n = len(height)
        if n <= 2:
            return 0

        max_l = [height[0]]
        max_r = [height[-1]]

        for i in range(1, n):
            max_l.append(max(max_l[-1], height[i]))
            max_r.append(max(max_r[-1], height[n-i-1]))

        # max_r.reverse()

        rain_water = 0
        for i in range(1, n-1):

            if max_r[n-i-1] > height[i] and max_l[i] > height[i]:
                rain_water += (min(max_r[n-i-1], max_l[i])-height[i])

        return rain_water



"""
Most Optimal solution

1, 0, 3, 2, 4

l, r = 0, n-1

max_l, max_r = 0, 0

/////// Approach ////////

we will iterate until l<=r
  now check if height[l] <= height[r]:
    then 
      if height[l] < max_l: add the diff in the res
      else: max_l + height[l]
      increse l
    
    else:
      if height[r] < max_r:
        add diff in the res
      else:
        max_r = height[r]
      
      decrese r
""" 
def solution2(height):
  l, r = 0, n-1
  max_l, max_r = 0, 0
  res = 0
  while l<=r:
      if height[l] <= height[r]:
        if height[l] < max_l:
          res += max_l - height[l]
        else:
            max_l = height[l]
        
      else:
          if height[r] < max_r:
            res += max_r - height[r]
          else:
              max_r = height[r]

  return res



