# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # q is the greater node of the two
        if p.val > q.val:
            q,p = p,q
        if root.val == p.val:
            return p
        if root.val == q.val:
            return q
        if q.val < root.val:
            return self.lowestCommonAncestor(root.left,p,q)
        if p.val > root.val:
            return self.lowestCommonAncestor(root.right,p,q)
        return root