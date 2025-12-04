
"""
Approach

array is sorted form so we find the mid element of the array
mid = len(arr)//2

make it the TreeNode and call for the function for the left and rigth sub tree recursively
During calling recursively we need to devide the given array into two part

Base Condition

if the given array is empty then return None 


"""
class TreeNode(object):
    def __init__(self, val=None, right=None, left=None):
        self.val=val
        self.right=right
        self.left=left
    
def arr_2_BST(self, l):
    # if list is empty
    totalnum=len(l)
    if not totalnum:
        return None

    #find the mid of the list
    mid=totalnum//2
    node=TreeNode(l[mid])
    node.left=self.arr_2_BST(l[:mid])
    node.right=self.arr_2_BST(l[mid+1:])

    return node
