class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        mp=set()
        while head is not None:
            if head in mp:
                return True 
            mp.add(head)
            head = head.next
        return False    
         