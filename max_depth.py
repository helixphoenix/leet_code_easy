class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, t1: TreeNode) -> int:
        if t1 == None:
          return 0 
        left=self.maxDepth(t1.left)
        right=self.maxDepth(t1.right)
        max_depth=max(left, right) + 1
        return max_depth