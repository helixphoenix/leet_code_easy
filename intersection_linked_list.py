class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        nodes_in_B = set()
 
        while headB is not None:
            nodes_in_B.add(headB)
            headB = headB.next
    
        while headA is not None:
            if headA in nodes_in_B:
                return headA
            headA = headA.next
    
        return None