

"""
Docstring for String.KMP_algo

# Concept: we have to find out the suffix which is also the prefix of the sub string
i = 0; j = 1
s = a b c d a b c a
    0 0 0 0 1 2 3 1



we create an array which hold the ind to which we have to start matching the sub string
"""
needle = 'abcdabya'
m = len(needle)

#  this code create the Longest prefix suffix array 
arr = [0]*m
i = 0
j = 1

while j < m:
    if needle[i] == needle[j]:
        i += 1
        arr[j] = i
        j+=1
    else:
        if i != 0:
            i = arr[i-1]
        else:
            j+=1

# find the straing index of the substring in the given text
text = ""
n = len(text)
i, j = 0, 0
while i < n:

  if needle[j] == needle[i]:
    j+=1
  elif j != 0:
    j = arr[j-1]
    continue

  if j == m:
    return True
  
  i+=1



