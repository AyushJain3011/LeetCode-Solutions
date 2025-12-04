def combinationSum2( arr, target) :
    # arr.sort()
    result=[]
    l=[]
    comb(0,arr, target, result, l)
    return result

def comb(ind, arr, target, result, l):
    if target<0: return
        
    if target==0:
        a=l.copy()
        a.sort()
        if not a in result:
            result.append(list(a))
        return

    if ind==len(arr):return

    for i in range(ind, len(arr)):
        l.append(arr[i])
        comb(i+1, arr, target-arr[i], result, l)
        l.pop()


print(combinationSum2([2,5,2,1,2], 5))