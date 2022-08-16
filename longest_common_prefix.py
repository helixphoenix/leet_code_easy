from difflib import SequenceMatcher

class Solution:
    
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        common=""
        if len(strs)==1:
            return strs[0]
        elif len(strs)==0:
            return common
        else:
            strs.sort()
            for i in range(len(strs[0])):
                if strs[0][i]==strs[-1][i]:
                    common += strs[0][i]
                else:
                    break
        return common     
                    
        

                