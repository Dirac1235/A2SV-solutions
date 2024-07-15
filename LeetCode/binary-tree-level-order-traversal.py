# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from queue import Queue  
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        superlis= []
        queue = Queue()
        queue.put([root])

        while not queue.empty():
            lis = []
            newnode = []
            nodelis = queue.get()
            for node in nodelis:
                if node:
                    lis.append(node.val)
                    newnode.append(node.left)
                    newnode.append(node.right)
            if lis:
                superlis.append(lis)
            if newnode:
                queue.put(newnode)
        return superlis
