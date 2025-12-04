A=[[1,2],[3,5],[6,7],[8,10],[12,16]]
B=[4,8]
A.append(B)
A.sort(key = lambda i:i[0])
print(A)
result=[]
result.append(A[0])
i=0

for ind in range(1, len(A)):
    if result[i][1]>=A[ind][0]:
        result.append([result[i][0], max(A[ind][1], result[i][1])])
        result.pop(i)

    else:
        result.append(A[ind])
        i+=1
print(result)
        
