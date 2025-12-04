d={}
n=0  # no of the distinct char
str="a"
# create a dictionary with reach char has value 0 and n hold the dictinct char count
for char in str:
    if char not in d:
        d[char]=0
        n+=1

i=0; j=1
d[str[i]]=1 # initialixing the first cahr of string is visited
count = 1  # count is one b/c first char is visited
ans=len(str)  # assign max length of the str

for j in range(1, len(str)):
    # increaing the value of the count when we face a new char whose key is 0
    if d[str[j]]==0:
        count+=1
    # otherwise increment the value of the key
    d[str[j]]+=1
    

    # now count == no of distinct char
    while count==n:
        # assign the diff of (j-i) to the ans
        ans=min(ans, j-i+1)
        # print(i, j, ans)
        # value of key became 0 then decrese the count
        if d[str[i]]==1:
            count-=1
        d[str[i]]-=1
        i+=1

print(ans)