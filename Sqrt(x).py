class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x
        start=0
        end = x
        while start<=end:
            mid = (start+end)//2
            mid_square=mid*mid 
            
            if mid_square== x:
                return mid
            if mid_square< x:
                start= mid+1
            else:
                end= mid-1
        return start-1      
                
