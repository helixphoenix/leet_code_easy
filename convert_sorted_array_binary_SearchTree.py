class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def treer(left,right): 
            if left > right: 
                return None 
            
            mid =(left + right) // 2 
            root= TreeNode(nums[mid])
            root.left=treer(left,mid-1)
            root.right=treer(mid+1,right)
            return root 
        
        return treer(0, len(nums)-1)

            