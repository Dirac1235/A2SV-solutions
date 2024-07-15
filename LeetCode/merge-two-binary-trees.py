# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        def merger(node, node2):
            if node and node2:
                node.val = node.val + node2.val
                node.left = merger(node.left, node2.left)
                node.right = merger(node.right, node2.right)
                return node
            elif not node and node2:
                return node2
            elif node and not node2:
                return node
            elif not node and not node2:
                return None
        root1 = merger(root1, root2)
        return root1
