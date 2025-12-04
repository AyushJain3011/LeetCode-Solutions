A=[0,1,0,2,1,0,1,3,2,1,2,1]
n=len(A)
r_max=[0]*n
l_max=[0]*n
l_max[0]=A[0]
r_max[n-1]=A[n-1]

max_water=0

for i in range(1, n):
    l_max[i]=max(A[i], l_max[i-1])

for i in range(n-2,-1,-1):
    r_max[i]=max(A[i], r_max[i+1])
    
print(l_max,"\n", r_max)

for i in range(n):
    max_water=max_water+min(l_max[i], r_max[i])-A[i]
    
print(max_water)