class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1 or n==2:
            return n
        previous_previous=1
        previous=2
        current=0
        for step in range(3,n+1):
            current=previous_previous+previous
            previous_previous=previous
            previous=current
        return current     
            
