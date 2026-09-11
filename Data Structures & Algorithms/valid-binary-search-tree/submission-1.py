# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def valid(root,mi,ma):
            if not root: 
                return True
            if mi < root.val < ma:
                return valid(root.left,mi,root.val) and valid(root.right,root.val,ma)  
            return False

        return valid(root,-1000,1000)