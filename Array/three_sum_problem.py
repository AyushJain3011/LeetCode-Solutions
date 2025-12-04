# hash_map = {}
        # for val in nums:
        #     if val in hash_map.keys():
        #         count = hash_map[val] + 1
        #         hash_map[val] = count
        #     else:
        #         hash_map[val] = 1

        # result = []
        # for i in range(len(nums)):
        #     hash_map[nums[i]] -= 1
        #     for j in range(i+1, len(nums)):
        #         hash_map[nums[j]] -= 1
        #         c = -(nums[i] + nums[j])

        #         if c in hash_map.keys() and hash_map[c] != 0:
        #             set_num = [nums[i], nums[j], c]
        #             set_num.sort()
        #             if set_num not in result:
        #                 result.append(set_num)

        #         hash_map[nums[j]] += 1
        #     hash_map[nums[i]] += 1

        # return result



def threeSum(nums):

    start = 0
    high = len(nums)-1
    target = []
    a=b=c=-100
    nums.sort()

    while start < len(nums):
        if a != nums[start]:
            a = nums[start]
            low = start + 1
            high = len(nums)-1

            while low < high:
                # if nums[low] == b:
                #     low+=1
                # elif nums[high] == c:
                #     high-=1
                # else:
                b = nums[low]
                c = nums[high]
                if b + c == -a:
                    target.append([a, b, c])
                    low += 1
                    high -= 1
                else: 
                    if b + c > -a:
                        high -= 1
                    else:
                        low += 1
            
        start += 1
    result = []
    for triplet in target:
        if triplet not in result:
            result.append(triplet)

    return result
        
# import sys
import math
# a = -sys.maxsize
# print(a)
v_max = float('inf')  # ---> this id for positive max_value
v_min = float('-inf')  # ---> this id for negative value
print(v_max > 12)
print(v_min > 12)
