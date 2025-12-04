left = 0
pivot=-1
right = len(nums)-1

# finding the pivot
while left < right:
    mid = (left+right)//2

    if mid>0 and nums[mid-1] > nums[mid]:
        pivot=mid
        break

    elif (mid+1)<len(nums) and nums[mid]>nums[mid+1]:
        pivot=mid
        break
    
    else:
        if nums[left] > nums[mid]:
            right = mid-1
        else:
            left = mid+1


# finding the accurate vlue of left an d right
left = 0
if pivot==-1:
    left=0; right=len(nums)-1
elif nums[pivot]==target:
    return pivot
else:
    if target < nums[left]:
        left=pivot+1
        right=len(nums)-1
    else:
        left=0
        right=pivot-1


#searching for the element if not present then
while left<=right:
    mid = (left+right)//2
    if nums[mid]==target:
        return mid
    else:
        if nums[mid] > target:
            right = mid-1
        else:
            left = mid+1