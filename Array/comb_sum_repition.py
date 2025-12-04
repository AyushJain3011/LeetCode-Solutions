result=[]
l=[]
def combinationSum2( arr, target):
    global result
    arr.sort()
    comb(0,arr, target)
    return result

def comb( ind, arr, target):
    global result, l
    if sum(l)==target:
        result.append(list(l))
        return


    for i in range(ind, len(arr)):
        if arr[i]<=target-sum(l):
            comb(i+1, arr, target)
            l.pop()

print(combinationSum2([10,1,2,7,6,1,5], 8))