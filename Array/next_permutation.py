result = []
def permutation(arr, s):
    global result
    if s == len(arr):
        result.append(list(arr))
        return

    for i in range(s, len(arr)):
        arr[i], arr[s] = arr[s], arr[i]
        permutation(arr, s+1)
        arr[s], arr[i] = arr[i], arr[s]

permutation(['a', 'b', 'c', 'd'], 0)
print(result)



# nums =[2, 3, 8, 5, 4, 1, 0]
# nums[2:]=reversed(nums[2:])
# print(nums)
# print(nums[2:])
# print(reversed(nums[2:]))
# print(nums[2:])

