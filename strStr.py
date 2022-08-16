class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        n=len(needle)
        h=list(haystack)
        
        for i in range(0,len(h)):
            if h[i] in needle:
                if h[i:i+n]==list(needle):
                    return i
        return -1