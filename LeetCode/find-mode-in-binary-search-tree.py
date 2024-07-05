# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        count = {}
        def dfs(node):
            if node:
                dfs(node.left)
                dfs(node.right)
                if node.val in count:
                    count[node.val] += 1
                else:
                    count[node.val] = 1
        dfs(root)
        mx = max(count.values())
        out = []
        for i in count:
            if count[i] == mx:
                out.append(i)
        return out
