# result=[]
# l=[]
# # count = 0
# def comination_sum(arr, target):
#     global result
#     global l
#     if sum(l)==target:
#         l.sort()
#         if not l in result:
#             result.append(list(l))
#             print(result)
#         return
        

#     else:
#         for i in range(len(arr)):
#             if arr[i] <= target-sum(l):
#                 l.append(arr[i])
#                 # print(l)
#                 comination_sum(arr, target)
#                 l.pop()

#     return result

# print(comination_sum([2,3,5], 8))

result=[]
l=[]
class Solution:
    def combinationSum(self, arr, target) :
        global result
        global l
        if sum(l)==target:
            l.sort()
            if not l in result:
                result.append(list(l))
            return
            
        else:
            for i in range(len(arr)):
                if arr[i] <= target-sum(l):
                    l.append(arr[i])
                    self.combinationSum(arr, target)
                    l.pop()

        return result


s1=Solution()
print(s1.combinationSum([2,3,5], 8))