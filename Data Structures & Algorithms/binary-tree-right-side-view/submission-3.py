# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        totalLevel = -1
        q = deque([(root,0)])
        if not root:
            return []
        while q:
            node,level = q.popleft()
            if node.right:
                q.append((node.right,level+1))
            if node.left:
                q.append((node.left,level+1))
            if node and level > totalLevel:
                res.append(node.val)
                totalLevel += 1

        return res