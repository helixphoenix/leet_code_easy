# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

# I can be placed before V (5) and X (10) to make 4 and 9. 
# X can be placed before L (50) and C (100) to make 40 and 90. 
# C can be placed before D (500) and M (1000) to make 400 and 900.



class Solution:
    
    
    
    def romanToInt(self, s: str) -> int:
        res=0
        rom_dic = {'M':1000, 'CM':900,'D':500,'CD':400,'C':100,'XC':90,'L':50, 'XL':40,'X':10,'IX':9,'VIII':8,'VII':7,'VI':6,'V':5,'IV':4,'III':3,'II':2,'I':1}
        reduct={'CM', 'CD', 'XC', 'XL','IX','IV'}
        
        if s in rom_dic:
            return rom_dic[s]
        
        else:
            for rom in reduct:
                if rom in s:
                    res+=rom_dic[rom]
                    s=s.replace(rom,"")
            for ro in s:
                res+=rom_dic[ro]
            
            return res

        
    