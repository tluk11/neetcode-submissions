# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def same(r,q):
            if not r and not q:
                return True
            if not r or not q:
                return False
            if r.val == q.val:
                return same(r.right,q.right) and same(r.left,q.left)
            return False
        if not root:
            return False
        if not subRoot:
            return True
        if same(root,subRoot):
            return True 
        return self.isSubtree(root.right,subRoot) or self.isSubtree(root.left,subRoot)