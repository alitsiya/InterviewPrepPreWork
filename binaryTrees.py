# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def chechHeadVerticalTraversal(root, s):
    if root.left == None and root.right == None:
        return False
    elif root.left == None:
        return verticalTraversal(root.right, s, root.val)
    elif root.right == None:
        return verticalTraversal(root.left, s, root.val)
    else:
        return verticalTraversal(root, s, 0)


def verticalTraversal(new_root, s, cur_s):
    if new_root is None:
        print cur_s
        return cur_s == s

    cur_s += new_root.val
    
    return verticalTraversal(new_root.left, s, cur_s) or verticalTraversal(new_root.right, s, cur_s)
    
    
        
# @param A : root node of tree
# @return a list of list of integers
def verticalOrderTraversal(A, s):
    if root.left == None and root.right == None:
        return False
    elif root.left == None:
        return verticalTraversal(root.right, s, root.val)
    elif root.right == None:
        return verticalTraversal(root.left, s, root.val)
    else:
        return verticalTraversal(root, s, 0)


 #      6
 #    /   \
 #   3     7
 #  / \     \
 # 2   5     9

#  [
#     [2],
#     [3],
#     [6 5],
#     [7],
#     [9]
# ]
# l1 = TreeNode(6)
# l2 = TreeNode(3)
# l3 = TreeNode(7)
# l4 = TreeNode(2)
# l5 = TreeNode(5)
# l6 = TreeNode(9)

# l1.left = l2
# l1.right = l3
# l2.left = l4
# l2.right = l5
# l3.right = l6

# 5 1000 200 -1 -1 -1 
# 1000
l1 = TreeNode(1000)
l2 = TreeNode(200)
l1.left = l2
print verticalOrderTraversal(l1, 1000)
