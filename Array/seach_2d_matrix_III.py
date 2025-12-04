# def searchMatrix(matrix: List[List[int]], t: int) -> bool:

#     c=0
#     r = len(matrix)-1

#     while c<len(matrix[0]):
#         if matrix[r][c]==t:
#             return True
#         elif r!=0 and matrix[r][c]>t:
#             r-=1
#         else:
#             c+=1
#     return False

# Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
# Output: true

def exist(b, w):
        h=v=0
        vl=len(b[0])-1
        hl=len(b)-1
        # print(hl, vl)

        return recu_search(h, v, hl, vl, b, w)

def recu_search(h, v, hl, vl, b, w):
    if not w:
        return True
    print(h, v)
    if b[h][v]==w[0]:
        w=w[1:]
    # print(w)
    if not h>hl and not v>vl:
        return recu_search(h+1, v, hl, vl, b, w)
        
        return recu_search(h-1, v+1, hl, vl, b, w)

print(exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED"))

# 0 0
# 1 0
# 2 0
# 1 1
# 2 1
# 1 2
# 2 2
# 1 3
# 2 3