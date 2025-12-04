"""
step1: iniitialize a variable with max val and i and ans equals to zero
step2: sort the given list
step3: check i ==0 or i>0 and i != i-1 element
step4: inintialize a var(low) to i+1 and another (high) to len(arr)-1
strp5: check low<high then add three numbers and assign it to a var.
step6: if sum equals to target then return sum otherwise compare max_diff to the (target-sum) if it is true the n
       assign max_diff to abs(target-sum) and ans equals to sum
step7: if sum < target increse low until low[i] != low[i+1] otherwise high -=1
step8: iterate through step3  until low >= high
step9: iterate till i < size of given array
step10: return ans
"""


def threeSumClosest(self, nums, target):
    max_diff = float('inf')
    i = 0
    nums.sort()

    while i < len(nums)-2:
        if i==0 or (i>0 and nums[i]!=nums[i-1]):
            low =  i+1
            high = len(nums)-1
            count = 0
            while low < high:
                # step5
                sum_3 = nums[i]+nums[low]+nums[high]
                # step6
                if target == sum_3:
                    return sum_3
                elif max_diff > abs(target-sum_3):
                    max_diff = abs(target-sum_3)
                    ans = sum_3

                if sum_3 < target:
                    low+=1
                    while low < high and nums[low] == nums[low-1]: low+=1
                else:
                    high-=1
                
        i+=1        

    return ans