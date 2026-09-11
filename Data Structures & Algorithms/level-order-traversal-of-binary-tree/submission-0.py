# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        toVisit, toVisit2 = [],[] #alternating lists 
        toVisit.append(root) 
        res = []
        if root is None:
            return []
        while toVisit or toVisit2:
            if toVisit: # visits first list
                temp = []
                for node in toVisit: 
                    temp.append(node.val)
                    if node.left: toVisit2.append(node.left)
                    if node.right: toVisit2.append(node.right)
                toVisit = []
                res.append(temp)
            elif toVisit2:
                temp = []
                for node in toVisit2:
                    temp.append(node.val)
                    if node.left: toVisit.append(node.left) 
                    if node.right: toVisit.append(node.right)
                toVisit2 = []
                res.append(temp)

        return res