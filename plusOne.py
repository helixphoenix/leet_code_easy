class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits.count(9) > 0:
            if len(digits)==digits.count(9):
                for i in range(len(digits)):
                    digits[i]=0
                digits.insert(0,1)   
            else:
                if digits[-1]== 9 and digits[-2]!= 9:
                        digits[-1]=0
                        digits[-2]+=1
                elif  digits[-1]== 9 and digits[-2]== 9:
                    last_nines=0
                    for i in range(1,len(digits)+1):
                        if digits[-i]==9:
                            last_nines+=1
                        else:
                            break
                    for n in range(1,last_nines+1):
                        digits[-n]=0
                    digits[-last_nines-1]+=1    
                else:
                    digits[-1]+=1

                    
        else :
            digits[-1]+=1
            
        return digits     
        
