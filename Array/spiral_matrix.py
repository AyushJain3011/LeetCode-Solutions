"""
1,2,3
4,5,6
7,8,9

[1,2,3,4,5,6,7,8,9]

approach:

first we traverse outer circle then we enter inside the matrix
"""

def spiralMatrix(A):
    top=left=0
    right=len(A[0])-1
    bottom=len(A)-1
    result=[]
    while left<right+1 and top<bottom+1:
        # i=top
        # for j in range(left,right+1):
        #     result.append(A[i][j])  
        
        # for i in range(top+1,bottom+1):
        #     result.append(A[i][j]) #i=2
        # if left+1!=right:
        #     for j in range(right-1, left-1, -1):
        #         result.append(A[i][j])


        # for i in range(bottom-1, top,-1):
        #     result.append(A[i][j])

        # top+=1;left+=1;bottom-=1;right-=1
        for j in range(top,right+1):
            result.append(A[top][j])  
        top+=1
        
        for i in range(top,bottom+1):
            result.append(A[i][j]) 

        right-=1

        if top < bottom+1:
            for j in range(right, left-1, -1): ######
                result.append(A[i][j])
            bottom-=1

        if left < right+1:
            for i in range(bottom, top-1,-1):
                result.append(A[i][j])
            left+=1

    return result


print(spiralMatrix([[1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13, 14,15,16]]))

print(spiralMatrix([[1,2,3],
    [5,6,7],
    [9,10,11]]))

    
