import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        word=re.sub('[^0-9a-zA-Z]+', '', s)
        word=word.lower()
        if word==word[::-1]:
            return True
        else:
            return False
        
class Solution:
    def isPalindrome(self, s:str) -> bool:
        word="".join(i for i in s if i.isalnum())
        word=word.lower()
        if word == word[::-1]:
            return True
        else:
            return False
        
        
        
            