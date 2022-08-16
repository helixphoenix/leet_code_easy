# Given an integer x, return true if x is palindrome integer.

# An integer is a palindrome when it reads the same backward as forward.

# For example, 121 is a palindrome while 123 is not.

import math

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if abs(x)!= x:
            return False
        if x<10:
            return True
        if x%10==0:
               return False     
        list_int=[x//(10**i)%10 for i in range(math.ceil(math.log(x,10))-1,-1,-1)]
        n=len(list_int)
        print(n)
        if n%2 == 0: 
            if list_int[:int(n/2)]==list_int[int(n/2):n][::-1]:
                return True
            else:
                return False
        else:

            if list_int[:int((n-1)/2)]==list_int[int((n-1)/2+1):][::-1]: 

                return True
            else:
                return False 