class Solution(object):
    def percentageLetter(self, s, letter):
        count =0
        
        for i in range(len(s)):
            if s[i]==letter:
                count += 1 
            
        self = ((count*100)/len(s))
        return self
